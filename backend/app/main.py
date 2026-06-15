from fastapi import FastAPI
from app.database import Base, engine
from app.routes.participant import router as participant_router

app = FastAPI(title="LISA Participant Tracker API")

Base.metadata.create_all(bind=engine)

app.include_router(participant_router, prefix="/participants", tags=["Participants"])


@app.get("/")
def root():
    return {"message": "LISA backend is running"}