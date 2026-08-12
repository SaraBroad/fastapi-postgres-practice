from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Patient


router = APIRouter(
    prefix="/patients",
    tags=["patients"],
)


@router.post("")
def create_patient(
    name: str,
    email: str,
    db: Session = Depends(get_db),
):
    patient = Patient(
        name=name,
        email=email,
    )

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient


@router.get("")
def get_patients(
    db: Session = Depends(get_db),
):
    patients = db.query(Patient).all()

    return patients