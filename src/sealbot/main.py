import sys

import hikari
import lightbulb
import pydantic

import sealbot.extensions
from sealbot.settings import Settings


def main() -> None:
    try:
        settings = Settings()
    except pydantic.ValidationError as e:
        print("Failed to validate settings: ", file=sys.stderr)

        for err in e.errors():
            loc = ".".join(str(loc) for loc in err["loc"])
            msg = err["msg"]
            typ = err["type"]
            print(f"  • {loc}: {msg} ({typ})", file=sys.stderr)

        sys.exit(1)

    bot = hikari.GatewayBot(
        token=settings.bot.token,
        logs=settings.logging.log_level,
    )
    client = lightbulb.client_from_app(bot)

    @bot.listen(hikari.StartingEvent)
    async def on_starting(_: hikari.StartingEvent) -> None:  # pyright: ignore[reportUnusedFunction]
        registry = client.di.registry_for(lightbulb.di.Contexts.DEFAULT)
        registry.register_value(Settings, settings)

        await client.load_extensions_from_package(sealbot.extensions)
        await client.start()

    bot.run()
