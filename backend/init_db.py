# backend/init_db.py
from backend.database import engine
from backend.models import (
    base,
    organization,
    object,
    device,
    device_type,
    power_source,
    power_source_type,
    battery,
    battery_type,
    note,
    user
)

def init():
    print("Inicializuji databázi...")
    base.Base.metadata.create_all(bind=engine)
    print("Hotovo.")

if __name__ == "__main__":
    init()
