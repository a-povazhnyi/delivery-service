from pydantic import BaseSettings


class Settings(BaseSettings):
    PORT: int = 8000
    HOST: str = '0.0.0.0'

    POSTGRES_USER: str = 'delivery'
    POSTGRES_DB: str = 'delivery'
    POSTGRES_PASSWORD: str = ''
    POSTGRES_HOST: str = 'db'
    POSTGRES_PORT: int = 5432
    DATABASE_URL: str


def get_settings():
    return Settings()


settings = get_settings()
