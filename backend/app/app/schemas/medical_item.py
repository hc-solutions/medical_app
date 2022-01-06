from typing import Optional

from pydantic import BaseModel


class MedicalItemBase(BaseModel):
    title: str
    medical_name: Optional[str]
    unit: str
    capacity: float
    amount: int
    expires_in_days: Optional[int]


class MedicalItemBaseCreate(MedicalItemBase):
    pass


class MedicalItemBaseUpdate(MedicalItemBase):
    pass


class MedicalItemInDBBase(MedicalItemBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class MedicalItem(MedicalItemInDBBase):
    pass


# Additional properties stored in DB
class MedicalItemInDB(MedicalItemInDBBase):
    pass
