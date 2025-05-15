from pydantic import BaseModel
from datetime import datetime

class NoteBase(BaseModel):
    object_id: int
    content: str

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
