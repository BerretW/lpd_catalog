from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.schemas.organization import Organization, OrganizationCreate
from backend.crud import organization as org_crud
from backend.auth import get_current_user
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Organization)
def create_organization(org: OrganizationCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return org_crud.create_organization(db, org)

@router.get("/", response_model=list[Organization])
def list_organizations(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return org_crud.get_organizations(db)
