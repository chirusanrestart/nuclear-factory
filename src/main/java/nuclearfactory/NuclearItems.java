package nuclearfactory;

import arc.graphics.Color;
import mindustry.type.Item;

public final class NuclearItems {
    public static Item uranium;
    public static Item plutonium;

    private NuclearItems() {
    }

    public static void load() {
        uranium = new Item("uranium", Color.valueOf("83c65a"));
        plutonium = new Item("plutonium", Color.valueOf("b56ad9"));
    }
}
