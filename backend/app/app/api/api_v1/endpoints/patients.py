from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas import PatientAppointment

router = APIRouter()


@router.get("/", response_model=List[schemas.Patient])
def read_patients(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    return crud.patient.get_multi(db, skip=skip, limit=limit)


@router.get("/{patient_id}", response_model=schemas.Patient)
def read_patient(
    patient_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    return crud.patient.get(db=db, id_=patient_id)


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


@router.get("/{patient_id}/procedures", response_model=List[schemas.ProcedureWithExp])
def get_patient_procedures(
    *,
    db: Session = Depends(deps.get_db),
    patient_id: int,
    expires_in_days: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    item = crud.patient.get(db=db, id_=patient_id)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return crud.patient.patient_procedures(
        db=db, patient_id=patient_id, will_expire_in=expires_in_days
    )


@router.get("/{patient_id}/appointments", response_model=List[PatientAppointment])
def get_patient_appointments(
    *,
    db: Session = Depends(deps.get_db),
    patient_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    return crud.patient.patient_appointments(
        db=db, patient_id=patient_id, skip=skip, limit=limit
    )


@router.patch("/", response_model=schemas.Patient)
def update_patient_in_db(
    *,
    db: Session = Depends(deps.get_db),
    patient_id: int,
    item_in: schemas.PatientUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update patient data.
    """

    item = crud.patient.get(db=db, id_=patient_id)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    item_ = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return item_
