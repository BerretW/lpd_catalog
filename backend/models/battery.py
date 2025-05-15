from sqlalchemy import Column, Integer, ForeignKey, Date, String, Text
from sqlalchemy.orm import relationship
from database import Base

class Battery(Base):
    __tablename__ = "batteries"

    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey("battery_types.id"))
    power_source_id = Column(Integer, ForeignKey("power_sources.id"))
    manufacture_date = Column(Date)
    install_date = Column(Date)
    custom_lifetime = Column(Integer)
    status = Column(String(50))  # OK, ke kontrole, na výměnu
    notes = Column(Text)

    battery_type = relationship("BatteryType")
    power_source = relationship("PowerSource", backref="batteries")
