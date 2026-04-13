from beet import Context
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenConfiguredCarver

from src.plugins.utils import iterate_versions


def beet_default(ctx: Context):
    vanilla = ctx.inject(Vanilla)

    for pack, version in iterate_versions(ctx):
        source = vanilla.releases[version].mount("data").data[WorldgenConfiguredCarver]
        patched = source["minecraft:canyon"].copy()

        # The probability that each chunk attempts to generate carvers.
        patched.data["config"]["probability"] = 0 # defaults to 0.01

        pack[WorldgenConfiguredCarver]["minecraft:canyon"] = patched
