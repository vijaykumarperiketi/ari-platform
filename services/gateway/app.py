from fastapi import FastAPI
from services.ingestion.service import IngestionService
from services.gateway.schemas import DocumentIn

app = FastAPI(title="ARI Platform API")
ingestion = IngestionService()

@app.post("/documents/ingest")
def ingest_document(doc: DocumentIn):
    ingestion.ingest(doc.model_dump())

@app.get("/health")
def health():
    return {"status": "ok"}
