import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("../.env.dev", "../src/.env.secret"),
        env_file_encoding="utf-8",
    )
    url: str
    user_kafka: str
    password_kafka: str
    topic: str


settings = Settings()

if __name__ == "__main__":
    print(settings.dict())