from sqlalchemy.orm import Session
from backend.models.power_source import PowerSource
from backend.schemas.power_source import PowerSourceCreate

def create_power_source(db: Session, ps: PowerSourceCreate):
    db_ps = PowerSource(**ps.dict())
    db.add(db_ps)
    db.commit()
    db.refresh(db_ps)
    return db_ps

def get_power_source(db: Session, ps_id: int):
    return db.query(PowerSource).filter(PowerSource.id == ps_id).first()

def get_power_sources(db: Session):
    return db.query(PowerSource).all()
