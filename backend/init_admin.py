# create_admin.py
from backend.database import SessionLocal
from backend.models.user import User
from passlib.context import CryptContext

# Konfigurace heslování
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_admin():
    db = SessionLocal()
    try:
        username = "admin"
        password = "775695905"  # Změň si pak na bezpečné heslo
        role = "admin"

        # Zkontroluj, zda už existuje
        existing = db.query(User).filter(User.username == username).first()
        if existing:
            print(f"Uživatel '{username}' už existuje.")
            return

        hashed_password = pwd_context.hash(password)
        user = User(username=username, hashed_password=hashed_password, role=role)
        db.add(user)
        db.commit()
        print(f"Admin uživatel '{username}' byl úspěšně vytvořen.")
    finally:
        db.close()

if __name__ == "__main__":
    create_admin()
