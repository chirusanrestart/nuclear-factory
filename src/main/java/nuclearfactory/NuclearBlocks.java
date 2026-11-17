package nuclearfactory;

import mindustry.world.Block;
import mindustry.world.blocks.environment.OreBlock;

public final class NuclearBlocks {
    public static Block oreUranium;
    public static Block orePlutonium;

    private NuclearBlocks() {
    }

    public static void load() {
        oreUranium = new OreBlock(NuclearItems.uranium) {{
            oreDefault = true;
            oreThreshold = 0.89f;
            oreScale = 27.5f;
        }};

        orePlutonium = new OreBlock(NuclearItems.plutonium) {{
            oreDefault = true;
            oreThreshold = 0.94f;
            oreScale = 34f;
        }};
    }
}
