import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class ProcedureBase(BaseModel):
    title: str
    created_at: datetime.datetime = datetime.datetime.now()


# Properties to receive via API on creation
class ProcedureCreate(ProcedureBase):
    pass


# Properties to receive via API on update
class ProcedureUpdate(ProcedureBase):
    pass


class ProcedureInDBBase(ProcedureBase):
    id: Optional[int]

    class Config:
        orm_mode = True


# Additional properties to return via API
class Procedure(ProcedureInDBBase):
    pass


# Additional properties stored in DB
class ProcedureInDB(ProcedureInDBBase):
    created_at: Optional[datetime.datetime]
