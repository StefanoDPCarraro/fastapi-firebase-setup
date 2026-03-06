import uuid
from typing import Any

from .irepository import IParentRepository


class ParentService:
    def __init__(self, repo: IParentRepository) -> None:
        self.repo = repo

    def register_parent(self, data: dict[str, Any]) -> dict[str, Any]:
        """Cria um responsável gerando ID e código de acesso."""
        data["id"] = data.get("id") or str(uuid.uuid4())
        data["access_code"] = str(uuid.uuid4())[:8].upper()
        return self.repo.save(data)
