# Usando a versão mais estável e leve para 2026
FROM python:3.12-slim

# Impede que o Python gere arquivos .pyc (economiza espaço e evita confusão)
ENV PYTHONDONTWRITEBYTECODE 1
# Garante que os logs do FastAPI apareçam em tempo real no console do Docker
ENV PYTHONUNBUFFERED 1
# Mostra ao testador onde esta o código para testar
ENV PYTHONPATH=/code

WORKDIR /code

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    git \
    make \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Camada de dependências (Cacheada pelo Docker se o arquivo não mudar)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Testes
RUN pip install --no-cache-dir \
    pytest \
    pytest-mock \
    pytest-asyncio \
    pytest-cov

# Copia o restante do código do projeto
COPY . .

# Expõe as portas: 8000 para API e 5678 para o Debugger (debugpy)
EXPOSE 8000
EXPOSE 5678
