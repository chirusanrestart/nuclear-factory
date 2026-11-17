package nuclearfactory;

import arc.graphics.Color;
import mindustry.type.Item;

public final class NuclearItems {
    public static Item uranium;
    public static Item plutonium;

    private NuclearItems() {
    }

    public static void load() {
        uranium = new Item("uranium", Color.valueOf("83c65a")) {{
            hardness = 4;
            cost = 1.2f;
            radioactivity = 0.8f;
        }};
        plutonium = new Item("plutonium", Color.valueOf("d58b55")) {{
            hardness = 5;
            cost = 1.5f;
            radioactivity = 1.2f;
        }};
    }
}
