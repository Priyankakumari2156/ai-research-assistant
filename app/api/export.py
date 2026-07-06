from fastapi import APIRouter

from app.schemas.export_schema import ExportRequest

from app.services.export_service import ExportService

router = APIRouter(
    prefix="/export",
    tags=["Export"]
)


@router.post("/markdown")
def export_markdown(request: ExportRequest):

    report = ExportService.generate_markdown(

        summary=request.summary,

        comparison=request.comparison,

        literature=request.literature,

        notes=request.notes,

        chat=request.chat,

    )

    return {

        "markdown": report

    }