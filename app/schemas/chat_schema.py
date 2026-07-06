from typing import  Optional
from pydantic import BaseModel


class ChatRequest(BaseModel):

    question: Optional[str] = None

    action: Optional[str] = None

    document_ids: Optional[list[str]] = None