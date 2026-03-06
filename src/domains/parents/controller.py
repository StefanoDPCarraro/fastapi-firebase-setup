from typing import Annotated

from fastapi import APIRouter, Depends

from .dtos import ParentCreate, ParentRead
from .repository import FirebaseParentRepository
from .service import ParentService

router = APIRouter(prefix="/parents", tags=["Parents"])


# DI (Injeção de Dependência)
def get_service() -> ParentService:
    return ParentService(FirebaseParentRepository())


@router.post("/", response_model=ParentRead, status_code=201)
def register_parent(
    schema: ParentCreate, service: Annotated[ParentService, Depends(get_service)]
) -> ParentRead:
    # O 'schema' aqui já chega validado pelo Pydantic
    return service.register_parent(schema)
