from beet import Context

from beet_datapack_utils import CARVER, targets, worldgen_config


def beet_default(ctx: Context):
    for target in targets(ctx):
        with target.patch(CARVER, "minecraft:canyon") as canyon:
            config = worldgen_config(canyon)

            # The probability that each chunk attempts to generate carvers.
            config["probability"] = 0  # defaults to 0.01