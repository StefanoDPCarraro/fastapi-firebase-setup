import uuid
from datetime import datetime
from typing import Any

from .irepository import IParentRepository


class ParentService:
    def __init__(self, repo: IParentRepository) -> None:
        self.repo = repo

    def register_parent(self, schema: Any) -> dict[str, Any]:
        # Se vier um objeto Pydantic, converte. Se já for dict skipa.
        data = schema.model_dump() if hasattr(schema, "model_dump") else schema

        """Cria um responsável gerando ID e código de acesso."""
        data["id"] = data.get("id") or str(uuid.uuid4())
        data["access_code"] = str(uuid.uuid4())[:8].upper()
        data["created_at"] = datetime.now()
        return self.repo.save(data)
