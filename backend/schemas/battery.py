from pydantic import BaseModel
from typing import Optional
from datetime import date

class BatteryBase(BaseModel):
    type_id: int
    power_source_id: int
    manufacture_date: Optional[date]
    install_date: Optional[date]
    custom_lifetime: Optional[int]
    status: Optional[str]
    notes: Optional[str]

class BatteryCreate(BatteryBase):
    pass

class Battery(BatteryBase):
    id: int

    class Config:
        from_attributes  = True
