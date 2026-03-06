from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# 1. Base: Campos que são comuns a todos os estados do dado
class ParentBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, examples=["João Silva"])
    email: EmailStr = Field(..., examples=["joao@email.com"])
    phone: str = Field(
        ...,
        pattern=r"^\+?[1-9]\d{1,14}$",
        examples=["+5554999998888"],
        description="Telefone no formato internacional E.164",
    )


# 2. Create: O que o usuário envia no cadastro (Input DTO)
class ParentCreate(ParentBase):
    password: str = Field(..., min_length=8, examples=["senha_segura123"])


# 3. Update: O que pode ser editado (campos opcionais)
class ParentUpdate(BaseModel):
    name: str | None = Field(None, min_length=3)
    phone: str | None = Field(None, pattern=r"^\+?[1-9]\d{1,14}$")
    # E-mail geralmente não se muda via update simples por segurança


# 4. Read: O que a API devolve (Output DTO)
class ParentRead(ParentBase):
    id: str
    access_code: str
    created_at: datetime

    # Permite converter objetos (como do Firebase ou Classes)
    # para Schema automaticamente
    model_config = ConfigDict(from_attributes=True)
