from beet import Context, DataPack
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenConfiguredCarver

CANYON = "minecraft:canyon"
PROBABILITY = 0 # defaults to 0.01


def beet_default(ctx: Context):
    source = get_source(ctx.inject(Vanilla), ctx.meta["base_version"])
    apply_patch(ctx.data, source)

    for directory, version in ctx.meta["overlay_versions"].items():
        overlay = ctx.data.overlays[directory]
        source = get_source(ctx.inject(Vanilla), version)
        apply_patch(overlay, source)


def get_source(vanilla: Vanilla, version: str):
    return vanilla.releases[version].mount("data").data[WorldgenConfiguredCarver]


def apply_patch(pack: DataPack, source):
    patched = source[CANYON].copy()

    config = patched.data["config"]
    config["probability"] = PROBABILITY

    pack[WorldgenConfiguredCarver][CANYON] = patched
