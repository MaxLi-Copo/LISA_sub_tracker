from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate

router = APIRouter(tags=["appointments"])


@router.post("/")
def create_appointment(appt: AppointmentCreate, db: Session = Depends(get_db)):

    new_appt = Appointment(**appt.dict())
    db.add(new_appt)
    db.commit()
    db.refresh(new_appt)

    return new_appt