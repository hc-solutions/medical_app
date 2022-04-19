from app.crud.base import CRUDBase
from app.models import Diseases
from app.schemas import DiseaseCreate, DiseaseUpdate


class CRUDDisease(CRUDBase[Diseases, DiseaseCreate, DiseaseUpdate]):
    pass


disease = CRUDDisease(Diseases)
