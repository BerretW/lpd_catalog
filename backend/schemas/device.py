from pydantic import BaseModel
from typing import Optional
from datetime import date

class DeviceBase(BaseModel):
    name: str
    type_id: int
    object_id: int
    serial_number: Optional[str]
    install_date: Optional[date]
    last_check: Optional[date]
    next_check: Optional[date]
    status: Optional[str]
    notes: Optional[str]

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int

    class Config:
        from_attributes  = True
