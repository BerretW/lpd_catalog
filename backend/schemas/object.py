from pydantic import BaseModel
from typing import Optional

class ObjectBase(BaseModel):
    name: str
    address: Optional[str]
    type: Optional[str]
    organization_id: int
    contact_name: Optional[str]
    contact_phone: Optional[str]
    contact_email: Optional[str]
    notes: Optional[str]

class ObjectCreate(ObjectBase):
    pass

class Object(ObjectBase):
    id: int

    class Config:
        from_attributes  = True
