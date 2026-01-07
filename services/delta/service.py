from services.common.database import SessionLocal
from services.common.models import Document

class DeltaService:
    def handle(self, document: dict):
        db = SessionLocal()

        record = db.query(Document).filter_by(
            document_id=document["document_id"]
        ).first()

        if not record:
            return  # shouldn't happen — ingestion guarantees existence

        event = Event(
            event_type=EVENTS["CONTENT_CHANGED"],
            timestamp=datetime.utcnow(),
            producer="delta",
            payload={
                "document_id": record.document_id,
                "version": record.version
            }
        )

        bus.publish(EVENTS["CONTENT_CHANGED"], event)
