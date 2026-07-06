from sentence_transformers import SentenceTransformer
import json


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def load_chunks(self, chunk_file):

        with open(chunk_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def generate_embeddings(self, chunks):

        texts = [c["text"] for c in chunks]

        return self.model.encode(
            texts,
            convert_to_numpy=True
        )