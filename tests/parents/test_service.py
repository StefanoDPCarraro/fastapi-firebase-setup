import pytest
from unittest.mock import MagicMock
from src.domains.parents.service import ParentService

def test_register_parent_generates_all_required_fields():
    # 1. Setup: Criamos um Mock do repositório (Interface Injection)
    mock_repo = MagicMock()
    # Simula o comportamento de salvar e retornar o dicionário
    mock_repo.save.side_effect = lambda data: data

    service = ParentService(repo=mock_repo)

    # Dados de entrada (o que viria do seu Schema/DTO)
    input_data = {
        "name": "João Silva",
        "email": "joao@email.com",
        "phone": "+5554999998888"
    }

    # 2. Execução
    result = service.register_parent(input_data)

    # 3. Asserções: Validando se os bugs que matamos continuam mortos
    assert "id" in result, "O ID deveria ter sido gerado pelo serviço"
    assert "access_code" in result, "O código de acesso de 8 dígitos deveria existir"
    assert len(result["access_code"]) == 8
    assert "created_at" in result, "O campo created_at é obrigatório para o response_model"
    assert result["name"] == "João Silva"

    # Garante que o repositório foi chamado exatamente uma vez
    mock_repo.save.assert_called_once()
