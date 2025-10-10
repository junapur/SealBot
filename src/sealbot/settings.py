import sys
from pathlib import Path
from typing import Literal

from pydantic import (
    BaseModel,
    DirectoryPath,
    Field,
    ValidationError,
)
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


def load_settings() -> Settings:
    try:
        return Settings()
    except ValidationError as e:
        print("Failed to validate settings:", file=sys.stderr)

        for err in e.errors():
            loc = ".".join(str(loc) for loc in err["loc"])
            msg = err["msg"]
            typ = err["type"]
            print(f"  • {loc}: {msg} ({typ})", file=sys.stderr)

        sys.exit(1)


def load_images(assets_dir: Path) -> list[Path]:
    image_exts = {".jpg", ".jpeg", ".png", ".avif", ".webp", ".gif"}

    images = [
        item
        for item in assets_dir.iterdir()
        if item.is_file() and item.suffix.lower() in image_exts
    ]

    if not images:
        print(f"Failed to find images in '{assets_dir}'", file=sys.stderr)
        print(f"Supported formats: {', '.join(sorted(image_exts))}", file=sys.stderr)
        sys.exit(1)

    return images


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
