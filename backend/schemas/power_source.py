from pydantic import BaseModel
from typing import Optional
from datetime import date

class PowerSourceBase(BaseModel):
    type_id: int
    device_id: int
    install_date: Optional[date]
    status: Optional[str]
    notes: Optional[str]

class PowerSourceCreate(PowerSourceBase):
    pass

class PowerSource(PowerSourceBase):
    id: int

    class Config:
        from_attributes  = True
