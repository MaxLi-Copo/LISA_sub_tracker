from pydantic import BaseModel
from datetime import date


class ParticipantCreate(BaseModel):
    subject_id: str
    email: str
    phone: str
    dob: date
    age_group: str | None = None


class ParticipantOut(BaseModel):
    id: int
    subject_id: str
    email: str
    phone: str
    dob: date
    age_group: str | None = None

    class Config:
        from_attributes = True