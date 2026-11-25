from beet import Context

from beet_datapack_utils import CARVER, get_config, versioned_packs


def beet_default(ctx: Context):
    for pack in versioned_packs(ctx):
        with pack.edit(CARVER, "minecraft:canyon") as canyon:
            # The probability that each chunk attempts to generate carvers.
            get_config(canyon)["probability"] = 0  # defaults to 0.01