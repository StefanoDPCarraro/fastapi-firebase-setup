.DEFAULT_GOAL := help

.PHONY: test test-failed test-cov show-cov clean-cov clean lint help

# 1. Rodar testes normal (Rápido, sem HTML)
test:
	pytest tests/

# 2. Rodar apenas testes falhados (Otimização para Debug)
test-failed:
	pytest --lf tests/

# 3. Rodar testes criando o HTML (Visão completa)
test-cov:
	pytest --cov=src --cov-report=html:cov_html tests/

# 4. Executar/Servir o HTML de cobertura
show-cov:
	@echo "🚀 Servindo cobertura em http://localhost:8080..."
	@cd cov_html && python3 -m http.server 8080

# 5. Limpar APENAS o HTML de cobertura
clean-cov:
	rm -rf cov_html/
	rm -f .coverage
	@echo "🧹 Relatório de cobertura removido."

# 6. Limpar tudo (Lixos gerais, caches e cobertura)
clean: clean-cov
	rm -rf .pytest_cache/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "✨ Todo o lixo de compilação foi limpo!"

# 7. Rodar o lint
lint:
	ruff check . --fix

# Menu de ajuda dinâmico
help:
	@echo "VanTrack CLI - Escolha uma ação:"
	@echo "  make test        - Executa testes rapidamente (sem coverage)"
	@echo "  make test-failed - Executa apenas os testes que falharam na última rodada"
	@echo "  make test-cov    - Executa testes e gera relatório HTML"
	@echo "  make show-cov    - Inicia servidor para ver o HTML (porta 8080)"
	@echo "  make clean-cov   - Remove apenas os arquivos de cobertura"
	@echo "  make clean       - Remove caches, pycache e cobertura"
	@echo "  make lint        - Formata e corrige estilo com Ruff"
