from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.schemas.user import User, UserCreate
from backend.crud import user as user_crud
from auth import create_access_token, get_current_user, require_roles

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(require_roles("admin"))):
    existing = user_crud.get_user_by_username(db, user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Uživatel již existuje")
    return user_crud.create_user(db, user)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Neplatné přihlašovací údaje")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
