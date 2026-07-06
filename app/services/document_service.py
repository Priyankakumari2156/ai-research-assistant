import fitz
from pathlib import Path


class DocumentService:

    @staticmethod
    def extract_text(pdf_path: str):

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        return text
