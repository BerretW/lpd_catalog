# models/organization.py
from sqlalchemy import Column, Integer, String, Text
from database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    ico = Column(String(32), nullable=True)
    dic = Column(String(32), nullable=True)
    address = Column(String(255), nullable=True)
    contact_name = Column(String(255), nullable=True)
    contact_phone = Column(String(50), nullable=True)
    contact_email = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
