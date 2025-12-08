package neluxx.no_more_ravines;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.resource.ResourceManagerHelper;
import net.fabricmc.fabric.api.resource.ResourcePackActivationType;
import net.fabricmc.loader.api.FabricLoader;
import net.minecraft.util.Identifier;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class NoMoreRavines implements ModInitializer {
	public static final String MOD_ID = "no-more-ravines";

	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

	@Override
	public void onInitialize() {
		LOGGER.info("Hello Fabric world!");

        ResourceManagerHelper.registerBuiltinResourcePack(
                Identifier.of(MOD_ID, "datapack"),
                FabricLoader.getInstance().getModContainer(MOD_ID).orElseThrow(),
                ResourcePackActivationType.ALWAYS_ENABLED
        );

        LOGGER.info("No more Ravines datapack registered!");
	}
}