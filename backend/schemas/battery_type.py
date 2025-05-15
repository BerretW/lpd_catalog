from pydantic import BaseModel
from typing import Optional

class BatteryTypeBase(BaseModel):
    name: str
    technology: Optional[str]
    manufacturer: Optional[str]
    capacity: Optional[str]
    voltage: Optional[str]
    default_lifetime: Optional[int]
    notes: Optional[str]

class BatteryTypeCreate(BatteryTypeBase):
    pass

class BatteryType(BatteryTypeBase):
    id: int

    class Config:
        from_attributes  = True
