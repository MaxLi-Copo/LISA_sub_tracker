from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate

router = APIRouter(prefix="/appointments", tags=["appointments"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_appointment(appt: AppointmentCreate, db: Session = Depends(get_db)):

    new_appt = Appointment(**appt.dict())
    db.add(new_appt)
    db.commit()
    db.refresh(new_appt)

    return new_appt