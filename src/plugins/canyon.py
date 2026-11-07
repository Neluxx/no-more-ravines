from beet import Context

from datapack_utils import CARVER, Targets, worldgen_config


def beet_default(ctx: Context):
    for target in ctx.inject(Targets):
        with target.patch(CARVER, "minecraft:canyon") as canyon:
            config = worldgen_config(canyon)

            # The probability that each chunk attempts to generate carvers.
            config["probability"] = 0  # defaults to 0.01