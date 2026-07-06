from fastapi import APIRouter, HTTPException

from app.services.document_manager import DocumentManager

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


# List all documents
@router.get("/")
def get_documents():
    return DocumentManager.list_documents()


# Get a single document
@router.get("/{document_id}")
def get_document(document_id: str):

    document = DocumentManager.get_document(document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document


# Delete a document
@router.delete("/{document_id}")
def delete_document(document_id: str):

    document = DocumentManager.get_document(document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return DocumentManager.delete_document(document_id)