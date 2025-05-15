from pydantic import BaseModel
from typing import Optional

class OrganizationBase(BaseModel):
    name: str
    ico: Optional[str]
    dic: Optional[str]
    address: Optional[str]
    contact_name: Optional[str]
    contact_phone: Optional[str]
    contact_email: Optional[str]
    notes: Optional[str]

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int

    class Config:
        from_attributes  = True
