from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4

class Event(BaseModel):
    event_id: str = str(uuid4())
    event_type: str
    timestamp: datetime
    producer: str
    payload: dict
