from fastapi import APIRouter, UploadFile, File
from app.services.pipeline_service import PipelineService
from typing import List



router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_pdfs(
    files: List[UploadFile] = File(...)):
    results = []

    for file in files:

        result = await PipelineService.process(file)

        results.append(result)

    return {
        "uploaded": len(results),
        "documents": results
    }