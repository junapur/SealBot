import platform
from datetime import datetime

import hikari
import lightbulb
import psutil
from hikari import SpacingType
from hikari.impl import (
    ContainerComponentBuilder,
    SeparatorComponentBuilder,
    TextDisplayComponentBuilder,
)

loader = lightbulb.Loader()


@loader.command
class Ping(
    lightbulb.SlashCommand,
    name="stats",
    description="Display statistics about the bot",
):
    @lightbulb.invoke
    async def invoke(
        self, ctx: lightbulb.Context, bot: hikari.GatewayBot, uptime: datetime
    ) -> None:
        process = psutil.Process()

        # TODO: rewrite this when lightbulb adds a components v2 builder
        components = [
            ContainerComponentBuilder(
                components=[
                    TextDisplayComponentBuilder(content="## SealBot"),
                    TextDisplayComponentBuilder(
                        content="A Discord bot for seal enjoyers."
                    ),
                    SeparatorComponentBuilder(
                        divider=True,
                        spacing=SpacingType.SMALL,
                    ),
                    TextDisplayComponentBuilder(
                        content=(
                            f"**Running on**: {platform.system()} {platform.release()}, "
                            f"{platform.python_implementation()} {platform.python_version()}"
                        )
                    ),
                    TextDisplayComponentBuilder(
                        content=f"**Uptime**: <t:{int(uptime.timestamp())}:R>"
                    ),
                    TextDisplayComponentBuilder(
                        content=f"**Latency**: {round(bot.heartbeat_latency * 1000)}ms"
                    ),
                    TextDisplayComponentBuilder(
                        content=f"**Memory**: {round(process.memory_info().rss / 1_000_000)}MB"
                    ),
                    TextDisplayComponentBuilder(
                        content=f"**CPU**: {round(process.cpu_percent())}%"
                    ),
                    TextDisplayComponentBuilder(
                        content=f"**Guilds**: {await bot.rest.fetch_my_guilds().count()}"
                    ),
                ]
            ),
            hikari.impl.MessageActionRowBuilder(
                components=[
                    hikari.impl.LinkButtonBuilder(
                        url="https://github.com/junapur/SealBot",
                        label="Source Code",
                    )
                ]
            ),
        ]
        await ctx.respond(components=components)
