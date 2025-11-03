"""Configuration settings (Pydantic BaseSettings).

Conteúdo mínimo para demonstrar leitura de variáveis de ambiente.
"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    api_key: str = ""
    database_url: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
