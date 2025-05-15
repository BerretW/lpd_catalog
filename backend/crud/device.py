from sqlalchemy.orm import Session
from backend.models.device import Device
from backend.schemas.device import DeviceCreate

def create_device(db: Session, dev: DeviceCreate):
    db_dev = Device(**dev.dict())
    db.add(db_dev)
    db.commit()
    db.refresh(db_dev)
    return db_dev

def get_device(db: Session, device_id: int):
    return db.query(Device).filter(Device.id == device_id).first()

def get_devices(db: Session):
    return db.query(Device).all()
