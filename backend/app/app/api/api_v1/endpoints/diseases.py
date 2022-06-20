from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Disease])
def read_disease(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    return crud.disease.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.Disease)
def create_disease(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.DiseaseCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new disease.
    """
    item = crud.disease.create(db=db, obj_in=item_in)
    return item
