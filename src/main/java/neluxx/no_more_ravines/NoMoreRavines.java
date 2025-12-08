package neluxx.no_more_ravines;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.resource.ResourceManagerHelper;
import net.fabricmc.fabric.api.resource.ResourcePackActivationType;
import net.fabricmc.loader.api.FabricLoader;
import net.minecraft.util.Identifier;

public class NoMoreRavines implements ModInitializer {
	public static final String MOD_ID = "no-more-ravines";

	@Override
	public void onInitialize() {
        ResourceManagerHelper.registerBuiltinResourcePack(
                Identifier.of(MOD_ID, "datapack"),
                FabricLoader.getInstance().getModContainer(MOD_ID).orElseThrow(),
                ResourcePackActivationType.ALWAYS_ENABLED
        );
	}
}