import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class PatientAppointmentsBase(BaseModel):
    record_id: int
    appointment_with: int
    valid_until: datetime.datetime
    took_place: bool
    scheduled_at: datetime.datetime
    started_at: Optional[datetime.datetime] = None
    ended_at: Optional[datetime.datetime] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime


# Properties to receive via API on creation
class PatientAppointmentCreate(PatientAppointmentsBase):
    pass


# Properties to receive via API on update
class PatientAppointmentUpdate(PatientAppointmentsBase):
    pass


class PatientAppointmentInDBBase(PatientAppointmentsBase):
    id: Optional[int]

    class Config:
        orm_mode = True


# Additional properties to return via API
class PatientAppointment(PatientAppointmentInDBBase):
    pass


# Additional properties stored in DB
class PatientAppointmentInDB(PatientAppointmentInDBBase):
    pass
