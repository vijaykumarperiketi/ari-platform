from pydantic import BaseModel

class DocumentIn(BaseModel):
    document_id: str
    title: str
    content: str
    metadata: dict
