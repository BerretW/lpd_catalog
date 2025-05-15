from sqlalchemy.orm import Session
from models.power_source_type import PowerSourceType
from schemas.power_source_type import PowerSourceTypeCreate

def create_power_source_type(db: Session, ptype: PowerSourceTypeCreate):
    db_type = PowerSourceType(**ptype.dict())
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type

def get_power_source_type(db: Session, type_id: int):
    return db.query(PowerSourceType).filter(PowerSourceType.id == type_id).first()

def get_power_source_types(db: Session):
    return db.query(PowerSourceType).all()
