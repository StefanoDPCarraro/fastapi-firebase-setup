from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # O Pydantic procura uma variável chamada FIREBASE_CREDENTIALS_PATH no .env
    firebase_credentials_path: str = Field(
        default="firebase-credentials.json", alias="FIREBASE_CREDENTIALS_PATH"
    )

    app_name: str = "VanTrack API"
    debug: bool = False

    # Configuração para ler o arquivo .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Instância única (Singleton) para ser usada no projeto todo
settings = Settings()
