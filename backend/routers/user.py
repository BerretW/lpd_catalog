from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Body
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.schemas.user import User, UserCreate
from backend.crud import user as user_crud
from backend.auth import create_access_token, get_current_user, require_roles, create_reset_token, verify_reset_token
from backend.email_utils import send_email
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

@router.post("/forgot-password")
def forgot_password(request: Request, email: str = Body(...), db: Session = Depends(get_db)):
    user = user_crud.get_user_by_username(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="Uživatel nenalezen")
    token = create_reset_token(user.username)
    reset_link = f"{request.base_url}reset-password?token={token}"
    send_email(user.username, "Reset hesla", f"Klikněte na odkaz pro reset hesla: {reset_link}")
    return {"message": "E-mail s odkazem na reset hesla byl odeslán."}

@router.post("/reset-password")
def reset_password(token: str = Body(...), new_password: str = Body(...), db: Session = Depends(get_db)):
    username = verify_reset_token(token)
    if not username:
        raise HTTPException(status_code=400, detail="Neplatný nebo expirovaný token")
    user = user_crud.get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="Uživatel nenalezen")
    user.hashed_password = pwd_context.hash(new_password)
    db.commit()
    return {"message": "Heslo bylo úspěšně změněno"}
