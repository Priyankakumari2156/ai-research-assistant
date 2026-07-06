from fastapi import APIRouter
from pydantic import BaseModel

from app.services.workspace_service import WorkspaceService

router = APIRouter(
    prefix="/workspace",
    tags=["Workspace"]
)

class WorkspaceUpdate(BaseModel):
    key: str
    value: str


class ChatEntry(BaseModel):
    question: str
    answer: str

@router.get("/")
def get_workspace():

    return WorkspaceService.load()



@router.post("/update")
def update_workspace(data: WorkspaceUpdate):

    WorkspaceService.update(
        data.key,
        data.value
    )

    return {
        "message": "Workspace updated successfully"
    }


@router.post("/chat")
def save_chat(chat: ChatEntry):

    WorkspaceService.add_chat(
        chat.question,
        chat.answer
    )

    return {
        "message": "Chat saved successfully"
    }