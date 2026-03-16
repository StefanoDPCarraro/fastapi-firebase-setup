from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import settings

# 1. O Engine: É quem realmente gerencia a conexão e o pool de conexões
# Ele usa a URL que definimos no seu .env
engine = create_engine(settings.database_url, echo=True)

# 2. SessionLocal: Uma fábrica de sessões.
# Cada requisição que chegar na sua API vai ganhar uma "sessão" própria.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 3. A Base: É a classe que seus Models (como o Parent) vão herdar.
# Ela é quem mapeia suas classes Python para tabelas no Postgres.
class Base(DeclarativeBase):
    pass


# 4. Dependência para as rotas do FastAPI (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
