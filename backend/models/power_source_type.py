from sqlalchemy import Column, Integer, String, Text
from backend.database import Base

class PowerSourceType(Base):
    __tablename__ = "power_source_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type = Column(String(100))  # např. UPS, trafo
    manufacturer = Column(String(255))
    model = Column(String(255))
    voltage = Column(String(50))
    current = Column(String(50))
    description = Column(Text)
