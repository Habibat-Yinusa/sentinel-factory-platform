from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import machine 
from app.api.v1.machines import router as machine_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sentinel Factory Platform",
    description="A cyber-physical systems monitoring and audit platform",
    version="0.1.0"
)

app.include_router(machine_router)

@app.get("/")
def health_check():
    return {"status": "ok", "system": "sentinel"}
