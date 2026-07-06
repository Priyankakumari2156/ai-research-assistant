import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))

    QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")

    MODEL_NAME = os.getenv("MODEL_NAME")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


settings = Settings()