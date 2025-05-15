from sqlalchemy import Column, Integer, String, Text
from database import Base

class BatteryType(Base):
    __tablename__ = "battery_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    technology = Column(String(50))  # např. olověná, Li-Ion
    manufacturer = Column(String(255))
    capacity = Column(String(50))    # např. 7Ah
    voltage = Column(String(50))     # např. 12V
    default_lifetime = Column(Integer)  # v měsících
    notes = Column(Text)
