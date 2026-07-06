from app.services.document_manager import DocumentManager
from app.services.notes_service import NotesService
from app.services.workspace_service import WorkspaceService


class DashboardService:

    @staticmethod
    def get_dashboard():

        documents = DocumentManager.list_documents()

        notes = NotesService.list()

        workspace = WorkspaceService.load()

        return {

            "documents": len(documents),

            "notes": len(notes),

            "chat_history": len(
                workspace.get("chat", [])
            ),

            "summary": bool(
                workspace.get("summary")
            ),

            "comparison": bool(
                workspace.get("comparison")
            ),

            "literature": bool(
                workspace.get("literature")
            ),

            "methodology": bool(
                workspace.get("methodology")
            ),

            "contributions": bool(
                workspace.get("contributions")
            ),

            "limitations": bool(
                workspace.get("limitations")
            ),

            "future_work": bool(
                workspace.get("future_work")
            ),

            "applications": bool(
                workspace.get("applications")
            )
        }