from beet import Context, DataPack
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenConfiguredCarver

CANYON = "minecraft:canyon"


def beet_default(ctx: Context):
    base_version = ctx.meta["base_version"]
    overlay_versions = ctx.meta["overlay_versions"]
    vanilla = ctx.inject(Vanilla)

    source = get_source(vanilla, base_version)
    apply_patch(ctx.data, source)

    for directory, version in overlay_versions.items():
        overlay = ctx.data.overlays[directory]
        source = get_source(vanilla, version)
        apply_patch(overlay, source)


def get_source(vanilla: Vanilla, version: str):
    return vanilla.releases[version].mount("data").data[WorldgenConfiguredCarver]


def apply_patch(pack: DataPack, source):
    patched = source[CANYON].copy()
    config = patched.data["config"]
    config["probability"] = 0
    pack[WorldgenConfiguredCarver][CANYON] = patched
