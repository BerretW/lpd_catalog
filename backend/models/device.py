from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type_id = Column(Integer, ForeignKey("device_types.id"))
    object_id = Column(Integer, ForeignKey("objects.id"))
    serial_number = Column(String(100))
    install_date = Column(Date)
    last_check = Column(Date)
    next_check = Column(Date)
    status = Column(String(50))
    notes = Column(Text)

    device_type = relationship("DeviceType")
    object = relationship("Object", backref="devices")
