from sqlalchemy.orm import Session
from backend.models.battery import Battery
from backend.schemas.battery import BatteryCreate

def create_battery(db: Session, bat: BatteryCreate):
    db_bat = Battery(**bat.dict())
    db.add(db_bat)
    db.commit()
    db.refresh(db_bat)
    return db_bat

def get_battery(db: Session, battery_id: int):
    return db.query(Battery).filter(Battery.id == battery_id).first()

def get_batteries(db: Session):
    return db.query(Battery).all()
