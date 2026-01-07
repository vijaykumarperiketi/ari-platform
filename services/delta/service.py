from services.events.bus import EventBus
from services.events.models import Event
from services.events.topics import EVENTS
from services.common.logger import get_logger
from datetime import datetime

log = get_logger("delta")
bus = EventBus()

class DeltaService:
    def handle(self, document: dict):
        log.info("Checking delta")

        # Placeholder for real hashing + version logic
        changed = True

        if changed:
            event = Event(
                event_type=EVENTS["CONTENT_CHANGED"],
                timestamp=datetime.utcnow(),
                producer="delta",
                payload=document
            )
            bus.publish(EVENTS["CONTENT_CHANGED"], event)
