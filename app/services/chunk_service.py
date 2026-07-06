import json
from pathlib import Path


class ChunkService:

    CHUNK_DIR = Path("uploads/chunks")

    @staticmethod
    def chunk_text(text, chunk_size=500, overlap=100):

        words = text.split()

        chunks = []

        start = 0
        chunk_id = 1

        while start < len(words):

            end = start + chunk_size

            chunk_text = " ".join(words[start:end])

            chunks.append({
                "chunk_id": chunk_id,
                "text": chunk_text,
                "word_count": len(chunk_text.split())
            })

            chunk_id += 1
            start += chunk_size - overlap

        return chunks

    @staticmethod
    def save_chunks(document_id, chunks):

        ChunkService.CHUNK_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = ChunkService.CHUNK_DIR / f"{document_id}.json"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                chunks,
                file,
                indent=4,
                ensure_ascii=False
            )

        return file_path