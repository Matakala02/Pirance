from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    access_token_expire_minutes: int = 30
    cors_origins: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()