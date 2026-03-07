.PHONY: test lint clean help

# Roda todos os testes com relatório de cobertura
test:
	pytest --cov=src tests/

# Roda apenas os testes que falharam na última vez (útil para debug rápido)
test-failed:
	pytest --lf

# Limpa arquivos temporários do Python
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f .pytest_cache

# Roda o Ruff para garantir que o código está limpo
lint:
	ruff check . --fix
