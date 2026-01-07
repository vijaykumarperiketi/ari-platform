import json
import redis
from services.events.models import Event

class EventBus:
    def __init__(self, host="redis", port=6379):
        self.client = redis.Redis(host=host, port=port, decode_responses=True)

    def publish(self, topic: str, event: Event):
        self.client.xadd(topic, event.model_dump())

    def consume(self, topic: str, group: str, consumer: str):
        self.client.xgroup_create(topic, group, mkstream=True)
        return self.client.xreadgroup(group, consumer, {topic: ">"}, count=10, block=5000)
