from fastapi import FastAPI

from database import Base, engine
from routes.patients import router as patients_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(patients_router)


@app.get("/")
def root():
    return {"message": "server is running"}