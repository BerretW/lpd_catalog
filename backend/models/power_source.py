from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.database import Base

class PowerSource(Base):
    __tablename__ = "power_sources"

    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey("power_source_types.id"))
    device_id = Column(Integer, ForeignKey("devices.id"))
    install_date = Column(Date)
    status = Column(String(50))
    notes = Column(Text)

    power_source_type = relationship("PowerSourceType")
    device = relationship("Device", backref="power_sources")
