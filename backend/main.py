# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import user, organization, device, object, note, battery, battery_type, device_type, power_source, power_source_type

app = FastAPI(title="Security Device API")

# CORS – můžeš omezit na frontend doménu
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Security Device API běží!"}

# Připojení jednotlivých routerů
app.include_router(user.router, prefix="/auth", tags=["Auth"])
app.include_router(organization.router, prefix="/organizations", tags=["Organizations"])
app.include_router(object.router, prefix="/objects", tags=["Objects"])
app.include_router(device.router, prefix="/devices", tags=["Devices"])
app.include_router(device_type.router, prefix="/device_types", tags=["Device Types"])
app.include_router(power_source.router, prefix="/power_sources", tags=["Power Sources"])
app.include_router(power_source_type.router, prefix="/power_source_types", tags=["Power Source Types"])
app.include_router(battery.router, prefix="/batteries", tags=["Batteries"])
app.include_router(battery_type.router, prefix="/battery_types", tags=["Battery Types"])
app.include_router(note.router, prefix="/notes", tags=["Notes"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
