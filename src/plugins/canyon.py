from beet import Context
from beet.contrib.vanilla import Vanilla

from src.plugins.utils import carver_registry, iterate_versions, worldgen_config


def beet_default(ctx: Context):
    vanilla = ctx.inject(Vanilla)

    for pack, version in iterate_versions(ctx):
        registry = carver_registry(version)
        source = vanilla.releases[version].mount("data").data[registry]
        patched = source["minecraft:canyon"].copy()
        config = worldgen_config(patched.data)

        # The probability that each chunk attempts to generate carvers.
        config["probability"] = 0 # defaults to 0.01

        pack[registry]["minecraft:canyon"] = patched
