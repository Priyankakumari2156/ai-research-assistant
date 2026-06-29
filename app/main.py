from fastapi import FastAPI

app = FastAPI(
    title="AI Research Assistant",
    description="Production-ready AI Research Assistant API",
    version="1.0.0"
)

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
