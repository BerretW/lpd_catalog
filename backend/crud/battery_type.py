from sqlalchemy.orm import Session
from backend.models.battery_type import BatteryType
from backend.schemas.battery_type import BatteryTypeCreate

def create_battery_type(db: Session, btype: BatteryTypeCreate):
    db_type = BatteryType(**btype.dict())
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type

def get_battery_type(db: Session, type_id: int):
    return db.query(BatteryType).filter(BatteryType.id == type_id).first()

def get_battery_types(db: Session):
    return db.query(BatteryType).all()
