from fastapi import APIRouter
from pydantic import BaseModel

from app.services.notes_service import NotesService

router = APIRouter(
    prefix="/notes",
    tags=["Research Notes"]
)


class NoteRequest(BaseModel):
    title: str
    content: str


@router.post("/")
def add_note(request: NoteRequest):

    return NotesService.add(
        request.title,
        request.content
    )


@router.get("/")
def get_notes():

    return NotesService.list()


@router.delete("/{note_id}")
def delete_note(note_id: str):

    NotesService.delete(note_id)

    return {
        "message": "Note deleted successfully."
    }