from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.participant import Participant
from pydantic import BaseModel
from datetime import date
from app.schemas.participant import ParticipantCreate, ParticipantOut

router = APIRouter()

@router.post("/")
def create_participant(data: ParticipantCreate, db: Session = Depends(get_db)):
    participant = Participant(
        subject_id=data.subject_id,
        email=data.email,
        phone=data.phone,
        dob=data.dob,
        age_group=data.age_group
    )
    db.add(participant)
    db.commit()
    db.refresh(participant)
    return participant


@router.get("/", response_model=list[ParticipantOut])
def get_participants(db: Session = Depends(get_db)):
    return db.query(Participant).all()