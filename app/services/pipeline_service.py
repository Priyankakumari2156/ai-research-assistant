from fastapi import UploadFile

from app.services.storage_service import StorageService
from app.services.document_service import DocumentService
from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class PipelineService:

    @staticmethod
    async def process(file: UploadFile):
        """
        Complete document ingestion pipeline.

        Steps:
        1. Save PDF
        2. Extract text
        3. Save extracted text
        4. Chunk text
        5. Save chunks
        """

        # Step 1: Save PDF
        pdf_info = await StorageService.save_pdf(file)

        # Step 2: Extract text
        text = DocumentService.extract_text(
            pdf_info["pdf_path"]
        )

        # Step 3: Save extracted text
        text_path = StorageService.save_text(
            pdf_info["document_id"],
            text
        )

        # Step 4: Create chunks
        chunks = ChunkService.chunk_text(text)

        # Step 5: Save chunks
        chunk_path = ChunkService.save_chunks(
            pdf_info["document_id"],
            chunks
        )

        # Step 6: Generate embeddings
        embedding_service = EmbeddingService()

        texts = [chunk["text"] for chunk in chunks]

        embeddings = embedding_service.model.encode(
            texts,
            convert_to_numpy=True
        )

        # Step 7: Store in Qdrant
        vector_service = VectorService()

        vector_service.create_collection()

        vector_service.insert_embeddings(
        document_id=pdf_info["document_id"],
        filename=pdf_info["original_filename"],
        chunks=chunks,
        embeddings=embeddings
    )

        # Return metadata
        return {
            "document_id": pdf_info["document_id"],
            "original_filename": pdf_info["original_filename"],
            "pdf_path": str(pdf_info["pdf_path"]),
            "text_path": str(text_path),
            "chunk_path": str(chunk_path),
            "total_chunks": len(chunks),
            "indexed": True,
            "characters": len(text),
            "status": "Document processed successfully"
        }