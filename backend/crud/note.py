from sqlalchemy.orm import Session
from models.note import Note
from schemas.note import NoteCreate

def create_note(db: Session, note: NoteCreate):
    db_note = Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes_for_object(db: Session, object_id: int):
    return db.query(Note).filter(Note.object_id == object_id).order_by(Note.created_at.desc()).all()
