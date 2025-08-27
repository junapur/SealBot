from typing import Literal

from pydantic import BaseModel, DirectoryPath, Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


class BotSettings(BaseModel):
    token: str
    assets_dir: DirectoryPath


class LogSettings(BaseModel):
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Settings(BaseSettings):
    bot: BotSettings = Field(default=...)
    logging: LogSettings = Field(default=...)
    model_config = SettingsConfigDict(toml_file="settings.toml", frozen=True)

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)
