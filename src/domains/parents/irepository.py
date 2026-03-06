from abc import ABC, abstractmethod
from typing import Any


class IParentRepository(ABC):
    @abstractmethod
    def save(self, data: dict[str, Any]) -> dict[str, Any]: ...

    @abstractmethod
    def get_by_id(self, parent_id: str) -> dict[str, Any] | None: ...
