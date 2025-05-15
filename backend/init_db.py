# init_db.py
from database import engine
from models import (
    base, organization, object, device, device_type,
    power_source, power_source_type, battery, battery_type
)

def init():
    print("Inicializuji databázi...")
    base.Base.metadata.create_all(bind=engine)
    print("Hotovo.")

if __name__ == "__main__":
    init()
