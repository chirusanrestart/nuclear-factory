#!/usr/bin/env python3
"""Generate three original 32x32 pixel-art variants for each ore."""
from pathlib import Path
import random
import struct
import zlib

OUT = Path("sprites/blocks")
OUT.mkdir(parents=True, exist_ok=True)

def write_png(path, pixels):
    size = len(pixels)
    raw = b"".join(b"\x00" + bytes(c for px in row for c in px) for row in pixels)

    def chunk(kind, data):
        return (struct.pack(">I", len(data)) + kind + data
                + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff))

    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">2I5B", size, size, 8, 6, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )

def make_ore(name, dark, light, seed):
    rng = random.Random(seed)
    size = 32
    pixels = [[(0, 0, 0, 0) for _ in range(size)] for _ in range(size)]
    centers = [(8, 8), (21, 8), (15, 18), (24, 24), (6, 25)]
    for cx, cy in centers:
        radius = rng.choice((2, 3, 4))
        for y in range(max(0, cy-radius-1), min(size, cy+radius+2)):
            for x in range(max(0, cx-radius-1), min(size, cx+radius+2)):
                if (x-cx)**2 + (y-cy)**2 <= radius*radius:
                    color = light if rng.random() > 0.32 else dark
                    pixels[y][x] = (*color, 255)
    for _ in range(15):
        x, y = rng.randrange(size), rng.randrange(size)
        if pixels[y][x][3] == 255:
            pixels[y][x] = (*light, 255)
    write_png(OUT / f"ore-{name}{seed % 3 + 1}.png", pixels)

for i, seed in enumerate((41, 42, 43)):
    make_ore("uranium", (65, 105, 42), (145, 205, 83), seed)
for i, seed in enumerate((73, 74, 75)):
    make_ore("plutonium", (115, 58, 38), (220, 145, 83), seed)
