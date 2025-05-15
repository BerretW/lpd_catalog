from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from schemas.battery_type import BatteryType, BatteryTypeCreate
from crud import battery_type as battype_crud
from auth import get_current_user, require_roles
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BatteryType)
def create_battery_type(bt: BatteryTypeCreate, db: Session = Depends(get_db), user = Depends(require_roles("admin"))):
    return battype_crud.create_battery_type(db, bt)

@router.get("/", response_model=list[BatteryType])
def list_battery_types(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return battype_crud.get_battery_types(db)
