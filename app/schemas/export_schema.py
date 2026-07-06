from typing import Optional
from pydantic import BaseModel


class ExportRequest(BaseModel):

    summary: Optional[str] = None

    comparison: Optional[str] = None

    literature: Optional[str] = None

    notes: Optional[str] = None

    chat: Optional[str] = None