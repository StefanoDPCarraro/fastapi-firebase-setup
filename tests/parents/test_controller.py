import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from src.main import app
from src.domains.parents.controller import get_service # Importe sua função de DI

client = TestClient(app)

# 1. Criamos um Mock para o Serviço
mock_service = MagicMock()

# 2. Forçamos o FastAPI a usar o Mock em vez do serviço real
app.dependency_overrides[get_service] = lambda: mock_service

def test_create_parent_endpoint_contract():
    # Setup do Mock para retornar o que o Pydantic espera
    payload = {
        "name": "Maria Oliveira",
        "email": "maria@email.com",
        "phone": "+5554988887777",
        "password": "senha_forte_123"
    }

    # Simulamos o retorno do serviço com os campos que o Pydantic exige
    mock_service.register_parent.return_value = {
        **payload,
        "id": "mock-uuid-123",
        "access_code": "ABC12345",
        "created_at": "2026-03-07T12:00:00"
    }

    # Execução
    response = client.post("/parents/", json=payload)

    # Verificações
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "maria@email.com"
    assert "access_code" in data

    # Limpa o override para não afetar outros testes (Boa prática!)
    app.dependency_overrides.clear()
