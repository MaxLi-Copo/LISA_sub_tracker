from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    participant_id = Column(Integer, ForeignKey("participants.id"))

    type = Column(String)  # cog / mri / pet
    start_time = Column(DateTime)
    end_time = Column(DateTime, nullable=True)

    status = Column(String, default="scheduled")  # scheduled / done / cancelled

    location = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())