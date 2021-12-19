from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud, models
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Patient])
def read_patients(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    return crud.patient.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.Patient)
def create_patient_in_db(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.PatientCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new patient.
    """
    item = crud.patient.create_patient(db=db, obj_in=item_in)
    return item
