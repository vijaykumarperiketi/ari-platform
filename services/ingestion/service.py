from services.events.bus import EventBus
from services.events.models import Event
from services.events.topics import EVENTS
from services.common.logger import get_logger
from datetime import datetime

log = get_logger("ingestion")
bus = EventBus()

class IngestionService:
    def ingest(self, document: dict):
        log.info("Ingesting document")

        event = Event(
            event_type=EVENTS["INGEST_COMPLETED"],
            timestamp=datetime.utcnow(),
            producer="ingestion",
            payload=document
        )

        bus.publish(EVENTS["INGEST_COMPLETED"], event)
