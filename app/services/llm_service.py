from google import genai
from app.config import settings


class LLMService:

    def __init__(self):

        if not settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate_answer(
        self,
        question: str,
        context: str
    ):

        prompt = f"""
You are an AI Research Assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, reply:

"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.client.models.generate_content(
            model=settings.MODEL_NAME,
            contents=prompt,
        )

        return response.text