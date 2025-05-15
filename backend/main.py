# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal

# Schemas
from schemas.organization import Organization, OrganizationCreate
from schemas.object import Object, ObjectCreate
from schemas.device import Device, DeviceCreate
from schemas.device_type import DeviceType, DeviceTypeCreate
from schemas.power_source import PowerSource, PowerSourceCreate
from schemas.power_source_type import PowerSourceType, PowerSourceTypeCreate
from schemas.battery import Battery, BatteryCreate
from schemas.battery_type import BatteryType, BatteryTypeCreate
from schemas.note import Note, NoteCreate
from schemas.user import User, UserCreate

# CRUD
import crud.organization as org_crud
import crud.object as obj_crud
import crud.device as dev_crud
import crud.device_type as devtype_crud
import crud.power_source as ps_crud
import crud.power_source_type as pstype_crud
import crud.battery as bat_crud
import crud.battery_type as battype_crud
import crud.note as note_crud
import crud.user as user_crud

# Auth
from auth import create_access_token, get_current_user, require_role

app = FastAPI()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Security Device API běží!"}

# --- Auth ---
@app.post("/register/", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(require_role("admin"))):
    existing = user_crud.get_user_by_username(db, user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Uživatel již existuje")
    return user_crud.create_user(db, user)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Neplatné přihlašovací údaje")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# --- Organizations ---
@app.post("/organizations/", response_model=Organization)
def create_organization(org: OrganizationCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return org_crud.create_organization(db, org)

@app.get("/organizations/", response_model=list[Organization])
def list_organizations(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return org_crud.get_organizations(db)

# --- Objects ---
@app.post("/objects/", response_model=Object)
def create_object(obj: ObjectCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return obj_crud.create_object(db, obj)

@app.get("/objects/", response_model=list[Object])
def list_objects(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return obj_crud.get_objects(db)

# --- Device Types ---
@app.post("/device_types/", response_model=DeviceType)
def create_device_type(devtype: DeviceTypeCreate, db: Session = Depends(get_db), user: User = Depends(require_role("admin"))):
    return devtype_crud.create_device_type(db, devtype)

@app.get("/device_types/", response_model=list[DeviceType])
def list_device_types(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return devtype_crud.get_device_types(db)

# --- Devices ---
@app.post("/devices/", response_model=Device)
def create_device(dev: DeviceCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return dev_crud.create_device(db, dev)

@app.get("/devices/", response_model=list[Device])
def list_devices(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return dev_crud.get_devices(db)

# --- Power Source Types ---
@app.post("/power_source_types/", response_model=PowerSourceType)
def create_power_source_type(pst: PowerSourceTypeCreate, db: Session = Depends(get_db), user: User = Depends(require_role("admin"))):
    return pstype_crud.create_power_source_type(db, pst)

@app.get("/power_source_types/", response_model=list[PowerSourceType])
def list_power_source_types(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return pstype_crud.get_power_source_types(db)

# --- Power Sources ---
@app.post("/power_sources/", response_model=PowerSource)
def create_power_source(ps: PowerSourceCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return ps_crud.create_power_source(db, ps)

@app.get("/power_sources/", response_model=list[PowerSource])
def list_power_sources(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return ps_crud.get_power_sources(db)

# --- Battery Types ---
@app.post("/battery_types/", response_model=BatteryType)
def create_battery_type(bt: BatteryTypeCreate, db: Session = Depends(get_db), user: User = Depends(require_role("admin"))):
    return battype_crud.create_battery_type(db, bt)

@app.get("/battery_types/", response_model=list[BatteryType])
def list_battery_types(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return battype_crud.get_battery_types(db)

# --- Batteries ---
@app.post("/batteries/", response_model=Battery)
def create_battery(bat: BatteryCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return bat_crud.create_battery(db, bat)

@app.get("/batteries/", response_model=list[Battery])
def list_batteries(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return bat_crud.get_batteries(db)

# --- Notes ---
@app.post("/notes/", response_model=Note)
def create_note(note: NoteCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return note_crud.create_note(db, note)

@app.get("/objects/{object_id}/notes/", response_model=list[Note])
def list_notes(object_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return note_crud.get_notes_for_object(db, object_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)