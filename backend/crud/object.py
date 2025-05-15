from sqlalchemy.orm import Session
from backend.models.object import Object
from backend.schemas.object import ObjectCreate

def create_object(db: Session, obj: ObjectCreate):
    db_obj = Object(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_object(db: Session, object_id: int):
    return db.query(Object).filter(Object.id == object_id).first()

def get_objects(db: Session):
    return db.query(Object).all()
