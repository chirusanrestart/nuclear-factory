# Nuclear Factory

Java mod for Mindustry v160.

## First milestone

- Uranium item and ore.
- Plutonium item and ore.
- Original pixel-art ore sprites generated during CI.
- GitHub Actions builds and uploads an Android-compatible mod JAR.

Thorium remains the vanilla Mindustry resource.

## Build locally

Use Java 17, Gradle, and an Android SDK with an installed Android platform and build-tools (including D8):

```sh
python3 tools/generate_sprites.py
gradle deploy
```

The installable cross-platform mod JAR is generated as `build/libs/NuclearFactory.jar`.
