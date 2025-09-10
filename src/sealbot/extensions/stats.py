import platform

import hikari
import lightbulb
import psutil

loader = lightbulb.Loader()


@loader.command
class Ping(
    lightbulb.SlashCommand,
    name="stats",
    description="Display statistics about the bot",
):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context, bot: hikari.GatewayBot) -> None:
        process = psutil.Process()

        components = [
            hikari.impl.ContainerComponentBuilder(
                components=[
                    hikari.impl.TextDisplayComponentBuilder(content="## Bot Stats"),
                    hikari.impl.SeparatorComponentBuilder(
                        divider=True,
                        spacing=hikari.SpacingType.SMALL,
                    ),
                    hikari.impl.TextDisplayComponentBuilder(
                        content=f"**Running on:** {platform.system()} {platform.release()}"
                    ),
                    hikari.impl.TextDisplayComponentBuilder(
                        content=f"**Using:** {platform.python_implementation()} {platform.python_version()}"
                    ),
                    hikari.impl.TextDisplayComponentBuilder(
                        content=f"**Guilds:** {await bot.rest.fetch_my_guilds().count()}"
                    ),
                    hikari.impl.TextDisplayComponentBuilder(
                        content=f"**Ping:** {round(bot.heartbeat_latency * 1000)}ms"
                    ),
                    hikari.impl.TextDisplayComponentBuilder(
                        content=f"**Memory:** {round(process.memory_info().rss / 1024 / 1024)}MB"
                    ),
                    hikari.impl.TextDisplayComponentBuilder(
                        content=f"**CPU:** {round(process.cpu_percent())}%"
                    ),
                ]
            ),
        ]

        await ctx.respond(components=components)
