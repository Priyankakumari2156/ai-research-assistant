from fastapi import APIRouter

from app.schemas.chat_schema import ChatRequest
from app.services.chat_service import ChatService
from app.services.workspace_service import WorkspaceService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

chat_service = ChatService()


@router.post("/")
def chat(request: ChatRequest):

    result = chat_service.ask(
        question=request.question,
        action=request.action,
        document_ids=request.document_ids
    )

    WorkspaceService.add_chat(
        request.question,
        result["answer"]
    )

    if request.action:
        WorkspaceService.update(
            request.action,
            result["answer"]
        )

    return result