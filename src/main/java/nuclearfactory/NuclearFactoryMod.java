package nuclearfactory;

import mindustry.mod.Mod;

public class NuclearFactoryMod extends Mod {
    @Override
    public void loadContent() {
        NuclearItems.load();
        NuclearBlocks.load();
    }
}
