from sqlalchemy import Column, String, Integer, DateTime, JSON
from datetime import datetime
from services.common.database import Base

class Document(Base):
    __tablename__ = "documents"

    document_id = Column(String, primary_key=True)
    version = Column(Integer)
    content_hash = Column(String)
    payload = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
