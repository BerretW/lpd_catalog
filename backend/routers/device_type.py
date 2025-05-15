from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from schemas.device_type import DeviceType, DeviceTypeCreate
from crud import device_type as devtype_crud
from auth import get_current_user, require_roles
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DeviceType)
def create_device_type(devtype: DeviceTypeCreate, db: Session = Depends(get_db), user = Depends(require_roles("admin"))):
    return devtype_crud.create_device_type(db, devtype)

@router.get("/", response_model=list[DeviceType])
def list_device_types(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return devtype_crud.get_device_types(db)
