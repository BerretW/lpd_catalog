from pydantic import BaseModel
from typing import Optional

class DeviceTypeBase(BaseModel):
    name: str
    category: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    description: Optional[str]

class DeviceTypeCreate(DeviceTypeBase):
    pass

class DeviceType(DeviceTypeBase):
    id: int

    class Config:
        from_attributes  = True
