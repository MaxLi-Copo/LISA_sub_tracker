from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(String, unique=True, index=True)

    email = Column(String, unique=True)
    phone = Column(String)
    dob = Column(Date)

    status = Column(String, default="active")
    notes = Column(String, nullable=True)