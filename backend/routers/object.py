from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from schemas.object import Object, ObjectCreate
from crud import object as obj_crud
from auth import get_current_user
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Object)
def create_object(obj: ObjectCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return obj_crud.create_object(db, obj)

@router.get("/", response_model=list[Object])
def list_objects(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return obj_crud.get_objects(db)
