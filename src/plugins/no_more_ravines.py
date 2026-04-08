from beet import Context, DataPack
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenConfiguredCarver

CANYON = "minecraft:canyon"


def beet_default(ctx: Context):
    config = ctx.meta["no_more_ravines"]
    vanilla = ctx.inject(Vanilla)

    _patch(ctx.data, vanilla, config["base_version"])

    for directory, version in config["overlay_versions"].items():
        overlay = ctx.data.overlays[directory]
        _patch(overlay, vanilla, version)


def _patch(pack: DataPack, vanilla: Vanilla, version: str):
    source = vanilla.releases[version].mount("data").data[WorldgenConfiguredCarver][CANYON]
    patched = source.copy()
    patched.data["config"]["probability"] = 0.0
    pack[WorldgenConfiguredCarver][CANYON] = patched
