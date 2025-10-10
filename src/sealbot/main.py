from datetime import datetime, timezone
from pathlib import Path

import hikari
import lightbulb

import sealbot.extensions
from sealbot.settings import load_images, load_settings


def main() -> None:
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

        uptime = datetime.now(timezone.utc)
        registry.register_value(datetime, uptime)

        await client.load_extensions_from_package(sealbot.extensions)
        await client.start()

    bot.run()
