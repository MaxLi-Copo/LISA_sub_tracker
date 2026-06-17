from sqlalchemy import Column, Integer, String, Date, Text
from app.database import Base

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    subject_id = Column(String, unique=True, nullable=False, index=True)

    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)
    dob = Column(Date, nullable=False)

    group = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    race = Column(String, nullable=False)
    edu_years = Column(Integer, nullable=True)

    status = Column(String, default="active")
    notes = Column(String, nullable=True)