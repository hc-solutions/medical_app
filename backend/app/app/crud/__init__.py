from .crud_item import item
from .crud_user import user

from .crud_patient import patient
from .crud_procedures import procedure
from .crud_medical_items import medical_item
from .crud_diseases import disease

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
