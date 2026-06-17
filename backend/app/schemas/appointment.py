from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    participant_id: int
    type: str
    start_time: datetime
    end_time: datetime | None = None
    location: str | None = None