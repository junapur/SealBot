import random
from pathlib import Path

import aiofiles
import hikari
import lightbulb

loader = lightbulb.Loader()


@loader.command
class Seal(
    lightbulb.SlashCommand,
    name="seal",
    description="Get a random image or gif of a seal",
):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context, images: list[Path]) -> None:
        image = random.choice(images)  # noqa: S311, not relevant in this context.

        async with aiofiles.open(image, "rb") as f:
            image_bytes = await f.read()

        await ctx.respond(hikari.Bytes(image_bytes, f"seal{image.suffix}"))
