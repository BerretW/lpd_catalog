from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.schemas.device import Device, DeviceCreate
from backend.crud import device as dev_crud
from backend.auth import get_current_user
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Device)
def create_device(dev: DeviceCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return dev_crud.create_device(db, dev)

@router.get("/", response_model=list[Device])
def list_devices(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return dev_crud.get_devices(db)
