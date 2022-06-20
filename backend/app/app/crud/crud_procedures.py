from typing import Any, Dict, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.patients import Procedures
from app.schemas.procedure import ProcedureCreate, ProcedureUpdate


class CRUDProcedure(CRUDBase[Procedures, ProcedureCreate, ProcedureUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Procedures,
        obj_in: Union[ProcedureUpdate, Dict[str, Any]]
    ) -> Procedures:
        raise AttributeError("You cant update procedures, only create new")


procedure = CRUDProcedure(Procedures)
