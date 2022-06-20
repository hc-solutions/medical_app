from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.MedicalItem])
def read_medical_item(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    return crud.medical_item.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.MedicalItem)
def create_medical_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.MedicalItemBaseCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new patient.
    """
    item = crud.medical_item.create(db=db, obj_in=item_in)
    return item
