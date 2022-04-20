from app.crud.base import CRUDBase
from app.models import MedicalItems
from app.schemas import MedicalItemBaseCreate, MedicalItemBaseUpdate


class CRUDMedicalItem(
    CRUDBase[MedicalItems, MedicalItemBaseCreate, MedicalItemBaseUpdate]
):
    pass


medical_item = CRUDMedicalItem(MedicalItems)
