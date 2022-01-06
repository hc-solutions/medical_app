import datetime
import uuid
from typing import Optional, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, func
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.patients import (
    Patients,
    Procedures,
    MedicalRecords,
    ProceduresRecords,
    PatientAppointments,
)
from app.schemas import PatientCreate, PatientUpdate


def create_urgent_patient(urgent_patient: PatientCreate):
    """Urgent patient - patient without any documents,
    without known first_name, middle_name, last_name or any

    :param urgent_patient:
    :return:
    """
    if urgent_patient.without_documents:
        patient_uuid = uuid.uuid4().__str__()
        urgent_patient.first_name = patient_uuid
        urgent_patient.last_name = patient_uuid
    return urgent_patient


class CRUDPatient(CRUDBase[Patients, PatientCreate, PatientUpdate]):
    def create_patient(self, db: Session, *, obj_in: PatientCreate) -> Patients:
        obj_in = create_urgent_patient(obj_in)
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def patient_procedures(
        db: Session, patient_id: int, will_expire_in: int
    ) -> Optional[List[Procedures]]:
        return (
            db.query(
                Procedures.id,
                Procedures.title,
                ProceduresRecords.created_at,
                Procedures.expires_in_days,
                ProceduresRecords.expires_at,
            )
            .join(ProceduresRecords, Procedures.id == ProceduresRecords.procedure_id)
            .join(MedicalRecords, ProceduresRecords.record_id == MedicalRecords.id)
            .filter(
                and_(
                    MedicalRecords.patient_id == patient_id,
                    func.date(ProceduresRecords.expires_at)
                    <= datetime.date.today() + datetime.timedelta(days=will_expire_in),
                    func.date(ProceduresRecords.expires_at) >= datetime.date.today(),
                )
            )
            .all()
        )

    @staticmethod
    def patient_appointments(
        db: Session, *, patient_id: int, skip: int = 0, limit: int = 100
    ) -> List[PatientAppointments]:
        return (
            db.query(PatientAppointments)
            .join(MedicalRecords, PatientAppointments.record_id == MedicalRecords.id)
            .filter(MedicalRecords.patient_id == patient_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


patient = CRUDPatient(Patients)
