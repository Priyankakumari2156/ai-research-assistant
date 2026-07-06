from pathlib import Path
from fastapi import UploadFile
import uuid

PDF_DIR = Path("uploads/pdfs")
TEXT_DIR = Path("uploads/processed")


class StorageService:

    @staticmethod
    async def save_pdf(file: UploadFile):

        PDF_DIR.mkdir(parents=True, exist_ok=True)

        document_id = str(uuid.uuid4())

        extension = file.filename.split(".")[-1]

        filename = f"{document_id}.{extension}"

        path = PDF_DIR / filename

        content = await file.read()

        with open(path, "wb") as f:
            f.write(content)

        return {
            "document_id": document_id,
            "pdf_path": path,
            "content": content,
            "original_filename": file.filename
        }

    @staticmethod
    def save_text(document_id: str, text: str):

        TEXT_DIR.mkdir(parents=True, exist_ok=True)

        path = TEXT_DIR / f"{document_id}.txt"

        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

        return path
