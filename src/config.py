from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Firebase
    firebase_credentials_path: str = Field(default="firebase-credentials.json", alias="FIREBASE_CREDENTIALS_PATH")

    # PostgreSQL
    # O alias garante que ele procure exatamente por DATABASE_URL no seu .env
    database_url: str = Field(alias="DATABASE_URL")

    app_name: str = "VanGO API"

    # Configuração para ler o arquivo .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignora outras variáveis no .env que não estão na classe
    )


# Instância única (Singleton) para ser usada no projeto todo
settings = Settings()
