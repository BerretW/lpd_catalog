from sqlalchemy.orm import Session
from models.device_type import DeviceType
from schemas.device_type import DeviceTypeCreate

def create_device_type(db: Session, dev: DeviceTypeCreate):
    db_dev = DeviceType(**dev.dict())
    db.add(db_dev)
    db.commit()
    db.refresh(db_dev)
    return db_dev

def get_device_type(db: Session, type_id: int):
    return db.query(DeviceType).filter(DeviceType.id == type_id).first()

def get_device_types(db: Session):
    return db.query(DeviceType).all()
