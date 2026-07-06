import uuid
from app.config import settings
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue
)


class VectorService:

    def __init__(self):
        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT
        )

    def create_collection(self):

        collections = self.client.get_collections()

        names = [c.name for c in collections.collections]

        if "documents" not in names:

            self.client.create_collection(
                collection_name="documents",
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

            print("Collection created")

        else:
            print("Collection already exists")

    def insert_embeddings(
        self,
        document_id,
        chunks,
        filename,
        embeddings
    ):

        points = []

        for chunk, embedding in zip(chunks, embeddings):

            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding.tolist(),
                    payload={
                        "document_id": document_id,
                        "chunk_id": chunk["chunk_id"],
                        "filename": filename,
                        "text": chunk["text"],
                        "word_count": chunk["word_count"]
                    }
                )
            )

        self.client.upsert(
            collection_name="documents",
            points=points
        )

        print(f"Inserted {len(points)} vectors.")


    def search(self, query_embedding, limit=5, document_ids=None):

        search_filter = None

        # Apply filter only if user selected documents
        if document_ids:

            search_filter = Filter(
            must=[
                Filter(
                    should=[
                        FieldCondition(
                            key="document_id",
                            match=MatchValue(value=document_id)
                        )
                        for document_id in document_ids
                    ]
                )
            ]
        )
        response = self.client.query_points(
            collection_name="documents",
            query=query_embedding.tolist(),
            query_filter=search_filter,
            limit=limit,
        )

        return response.points
    
    def delete_document(self, document_id):

        self.client.delete(
            collection_name="documents",
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="document_id",
                        match=MatchValue(value=document_id)
                    )
                ]
            )
        )

        print(f"Deleted vectors for document: {document_id}")