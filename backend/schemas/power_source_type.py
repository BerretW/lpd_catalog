from pydantic import BaseModel
from typing import Optional

class PowerSourceTypeBase(BaseModel):
    name: str
    type: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    voltage: Optional[str]
    current: Optional[str]
    description: Optional[str]

class PowerSourceTypeCreate(PowerSourceTypeBase):
    pass

class PowerSourceType(PowerSourceTypeBase):
    id: int

    class Config:
        from_attributes  = True
