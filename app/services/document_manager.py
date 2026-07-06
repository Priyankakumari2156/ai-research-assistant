from pathlib import Path
from app.services.vector_service import VectorService
import json


class DocumentManager:

    PDF_DIR = Path("uploads/pdfs")
    TEXT_DIR = Path("uploads/processed")
    CHUNK_DIR = Path("uploads/chunks")

    @staticmethod
    def list_documents():

        documents = []

        for pdf in DocumentManager.PDF_DIR.glob("*.pdf"):

            document_id = pdf.stem

            chunk_file = (
                DocumentManager.CHUNK_DIR /
                f"{document_id}.json"
            )

            total_chunks = 0

            if chunk_file.exists():

                with open(
                    chunk_file,
                    "r",
                    encoding="utf-8"
                ) as file:

                    chunks = json.load(file)

                total_chunks = len(chunks)

            documents.append(
                {
                    "document_id": document_id,
                    "filename": pdf.name,
                    "chunks": total_chunks
                }
            )

        return documents
    
    def get_document(document_id):

        pdf_file = DocumentManager.PDF_DIR / f"{document_id}.pdf"

        if not pdf_file.exists():
            return None

        chunk_file = DocumentManager.CHUNK_DIR / f"{document_id}.json"

        text_file = DocumentManager.TEXT_DIR / f"{document_id}.txt"

        chunks = []

        if chunk_file.exists():
            with open(chunk_file, "r", encoding="utf-8") as f:
                chunks = json.load(f)

        characters = 0

        if text_file.exists():
            with open(text_file, "r", encoding="utf-8") as f:
                text = f.read()
            characters = len(text)

        return {
            "document_id": document_id,
            "filename": pdf_file.name,
            "size_kb": round(pdf_file.stat().st_size / 1024, 2),
            "chunks": len(chunks),
            "characters": characters
        }
    

    def delete_document(document_id):

        pdf_file = DocumentManager.PDF_DIR / f"{document_id}.pdf"
        text_file = DocumentManager.TEXT_DIR / f"{document_id}.txt"
        chunk_file = DocumentManager.CHUNK_DIR / f"{document_id}.json"

        # Delete files
        if pdf_file.exists():
            pdf_file.unlink()

        if text_file.exists():
            text_file.unlink()

        if chunk_file.exists():
            chunk_file.unlink()

        # Delete vectors from Qdrant
        vector_service = VectorService()
        vector_service.delete_document(document_id)

        return {
            "message": "Document deleted successfully"
        }