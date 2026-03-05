from typing import Any

from .interfaces import IParentRepository


class ParentService:
    # ANN001: repo precisa ser do tipo IParentRepository
    # -> None: construtores sempre retornam None
    def __init__(self, repo: IParentRepository) -> None:
        self.repo = repo

    # ANN201: define que a função retorna um dicionário
    # ANN001: define que 'data' é um dicionário com chaves string
    def create(self, data: dict[str, Any]) -> dict[str, Any]:
        """Cria um novo registro de pai/responsável."""
        # Aqui você adicionaria lógicas como gerar ID ou Hash de senha
        return self.repo.save(data)
