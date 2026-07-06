
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.literature_service import LiteratureService
from app.services.workspace_service import WorkspaceService


router = APIRouter(
    prefix="/literature",
    tags=["Literature Review"]
)


class LiteratureRequest(BaseModel):
    document_ids: list[str]


service = LiteratureService()


@router.post("/")
def generate(request: LiteratureRequest):

    result = service.generate(
        request.document_ids
    )

    WorkspaceService.update(
        "literature",
        result["answer"]
    )

    return result