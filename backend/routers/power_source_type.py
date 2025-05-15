# backend/routers/power_source_type.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.schemas.power_source_type import PowerSourceType, PowerSourceTypeCreate
from backend.crud import power_source_type as pstype_crud
from backend.auth import get_current_user, require_roles

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PowerSourceType)
def create_power_source_type(pstype: PowerSourceTypeCreate, db: Session = Depends(get_db), user = Depends(require_roles("admin"))):
    return pstype_crud.create_power_source_type(db, pstype)

@router.get("/", response_model=list[PowerSourceType])
def list_power_source_types(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return pstype_crud.get_power_source_types(db)
