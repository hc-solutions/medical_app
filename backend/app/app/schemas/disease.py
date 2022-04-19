import datetime
from typing import Optional
from pydantic import BaseModel


# Shared properties
class DiseaseBase(BaseModel):
    code: str
    title: str
    source: int
    created_at: Optional[datetime.datetime] = datetime.datetime.now()


# Properties to receive via API on creation
class DiseaseCreate(DiseaseBase):
    pass


# Properties to receive via API on update
class DiseaseUpdate(DiseaseBase):
    pass


class PatientInDBBase(DiseaseBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Disease(PatientInDBBase):
    pass


# Additional properties stored in DB
class DiseaseInDB(PatientInDBBase):
    pass
