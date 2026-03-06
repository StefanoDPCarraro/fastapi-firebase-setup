from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Parent:
    """A Entidade de domínio 'Pai/Responsável'."""

    name: str
    email: str
    phone: str
    access_code: str
    id: str | None = None
    created_at: datetime = field(default_factory=datetime.now)

    def generate_access_code(self) -> str:
        # Lógica de negócio que pertence à entidade
        pass
