from sqlalchemy import Column, Integer, String, Text
from backend.database import Base

class DeviceType(Base):
    __tablename__ = "device_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(50))  # EZS, CCTV, EKV, MZS
    manufacturer = Column(String(255))
    model = Column(String(255))
    description = Column(Text)
