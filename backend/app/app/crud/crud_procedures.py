from typing import Dict, Any, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.schemas.procedure import ProcedureCreate, ProcedureUpdate
from app.models.patients import Procedures


class CRUDProcedure(CRUDBase[Procedures, ProcedureCreate, ProcedureUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: ProcedureUpdate,
        obj_in: Union[ProcedureUpdate, Dict[str, Any]]
    ) -> Procedures:
        raise AttributeError("You cant update procedures, only create new")


procedure = CRUDProcedure(Procedures)
