from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router   
from app.api.compare import router as compare_router
from app.api.documents import router as documents_router
from app.api.literature import router as literature_router
from app.api.notes import router as notes_router
from app.api.export import router as export_router
from app.api.dashboard import router as dashboard_router
from app.api import workspace


app = FastAPI(
    title="AI Research Assistant",
    description="Production-ready AI Research Assistant API",
    version="1.0.0"
)

# Register API routes
app.include_router(upload_router)
app.include_router(chat_router)  
app.include_router(documents_router)
app.include_router(compare_router)
app.include_router(literature_router)
app.include_router(notes_router)
app.include_router(export_router)
app.include_router(dashboard_router)
app.include_router(workspace.router)



@app.get("/")
def home():
    return {
        "project": "AI Research Assistant",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
