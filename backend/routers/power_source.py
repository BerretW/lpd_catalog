from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.schemas.power_source import PowerSource, PowerSourceCreate
from backend.crud import power_source as ps_crud
from auth import get_current_user
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PowerSource)
def create_power_source(ps: PowerSourceCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return ps_crud.create_power_source(db, ps)

@router.get("/", response_model=list[PowerSource])
def list_power_sources(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return ps_crud.get_power_sources(db)
