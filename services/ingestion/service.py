import hashlib
from services.common.database import SessionLocal
from services.common.models import Document

class IngestionService:
    def ingest(self, document: dict):
        db = SessionLocal()

        raw = str(document).encode()
        content_hash = hashlib.sha256(raw).hexdigest()

        existing = db.query(Document).filter_by(
            document_id=document["document_id"]
        ).first()

        if existing and existing.content_hash == content_hash:
            return  # Safe no‑op

        version = 1 if not existing else existing.version + 1

        record = Document(
            document_id=document["document_id"],
            version=version,
            content_hash=content_hash,
            payload=document
        )

        db.merge(record)
        db.commit()
