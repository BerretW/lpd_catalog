from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.schemas.battery import Battery, BatteryCreate
from backend.crud import battery as bat_crud
from backend.auth import get_current_user
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Battery)
def create_battery(bat: BatteryCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return bat_crud.create_battery(db, bat)

@router.get("/", response_model=list[Battery])
def list_batteries(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return bat_crud.get_batteries(db)
