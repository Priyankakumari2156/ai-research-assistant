from fastapi import APIRouter
from pydantic import BaseModel

from app.services.compare_service import CompareService
from app.services.workspace_service import WorkspaceService


router = APIRouter(
    prefix="/compare",
    tags=["Compare"]
)


class CompareRequest(BaseModel):
    document_ids: list[str]


service = CompareService()


@router.post("/")
def compare(request: CompareRequest):

    result = service.compare(
        request.document_ids
    )

    WorkspaceService.update(
        "comparison",
        result["answer"]
    )

    return result