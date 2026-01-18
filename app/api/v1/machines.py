from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.machine import Machine

router = APIRouter(prefix="/machines", tags=["Machines"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_machine(
    name: str,
    machine_type: str,
    location: str | None = None,
    db: Session = Depends(get_db)
):
    machine = Machine(
        name=name,
        machine_type=machine_type,
        location=location
    )
    db.add(machine)
    db.commit()
    db.refresh(machine)
    return machine

@router.get("/")
def list_machines(db: Session = Depends(get_db)):
    return db.query(Machine).all()
