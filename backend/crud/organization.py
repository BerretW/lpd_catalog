from sqlalchemy.orm import Session
from backend.models.organization import Organization
from backend.schemas.organization import OrganizationCreate

def create_organization(db: Session, org: OrganizationCreate):
    db_org = Organization(**org.dict())
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org

def get_organization(db: Session, org_id: int):
    return db.query(Organization).filter(Organization.id == org_id).first()

def get_organizations(db: Session):
    return db.query(Organization).all()
