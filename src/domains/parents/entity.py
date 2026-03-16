from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database import Base


class ParentModel(Base):
    __tablename__ = "parents"

    # ID Serial para chaves estrangeiras internas (mais rápido)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # UID do Firebase - O elo com a Autenticação
    firebase_uid: Mapped[str] = mapped_column(String(128), unique=True, index=True, nullable=False)

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    # Email único para buscas rápidas
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)

    phone: Mapped[str] = mapped_column(String(20), nullable=False)

    # O código de acesso que você mencionou na dataclass
    access_code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    # Deixa o PostgreSQL 16 gerenciar o timestamp automaticamente
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"<Parent(name={self.name}, email={self.email})>"
