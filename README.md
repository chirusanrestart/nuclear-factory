# Nuclear Factory

Java mod for Mindustry v160.

## First milestone

- Uranium item and ore.
- Plutonium item and ore.
- Original pixel-art ore sprites generated during CI.
- GitHub Actions build that publishes the mod JAR as an artifact.

Thorium remains the vanilla Mindustry resource.

## Build locally

Use Java 17 and Gradle:

```sh
python3 tools/generate_sprites.py
gradle build
```

The mod JAR is generated in `build/libs/`.
