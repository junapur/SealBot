import asyncio
import sys
import time
from pathlib import Path

import hikari
import lightbulb
import pydantic

import sealbot.extensions
from sealbot.settings import Settings


def main() -> None:
    if sys.platform != "win32":
        import uvloop

        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    settings = load_settings()
    images = load_images(settings.bot.assets_dir)

    bot = hikari.GatewayBot(
        token=settings.bot.token,
        logs=settings.logging.log_level,
    )

    client = lightbulb.client_from_app(bot)

    @bot.listen(hikari.StartingEvent)
    async def on_starting(_: hikari.StartingEvent) -> None:  # pyright: ignore[reportUnusedFunction]
        registry = client.di.registry_for(lightbulb.di.Contexts.DEFAULT)
        registry.register_value(list[Path], images)

        uptime = int(time.time())
        registry.register_value(int, uptime)

        await client.load_extensions_from_package(sealbot.extensions)
        await client.start()

    bot.run()


def load_settings() -> Settings:
    try:
        return Settings()
    except pydantic.ValidationError as e:
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
        print(f"No image files found in '{assets_dir}'", file=sys.stderr)
        sys.exit(1)

    return images
