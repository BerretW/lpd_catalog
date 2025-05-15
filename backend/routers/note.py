from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.note import Note, NoteCreate
from crud import note as note_crud
from auth import get_current_user
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Note)
def create_note(note: NoteCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return note_crud.create_note(db, note)

@router.get("/object/{object_id}", response_model=list[Note])
def list_notes(object_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return note_crud.get_notes_for_object(db, object_id)
