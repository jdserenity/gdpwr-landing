#!/usr/bin/env python3
"""Bake black/red/white Earth texture from assets/earth-map-natural.jpg.

Oceans -> black, land -> red, ice/clouds -> white accents.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
NATURAL = ROOT / "assets" / "earth-map-natural.jpg"
OUT = ROOT / "assets" / "earth-map.jpg"


def is_ocean(r: int, g: int, b: int) -> bool:
  # Blue Marble oceans are blue-dominant; catch dark seas too (no min-blue floor).
  if b > r + 4 and b > g + 2:
    return True
  # Deep / shadowed water: still bluer than red, not bright land.
  if b >= g and b > r and b < 90 and r < 70:
    return True
  return False


def recolor(src: Path, dest: Path) -> None:
  im = Image.open(src).convert("RGB")
  px = im.load()
  w, h = im.size
  for y in range(h):
    for x in range(w):
      r, g, b = px[x, y]
      lum = 0.299 * r + 0.587 * g + 0.114 * b
      if is_ocean(r, g, b):
        px[x, y] = (0, 0, 0)
      elif lum >= 205:
        px[x, y] = (245, 245, 245)
      elif lum >= 170:
        t = (lum - 170) / 35.0
        px[x, y] = (int(215 + 40 * t), int(30 + 200 * t), int(30 + 200 * t))
      else:
        t = max(0.35, min(1.0, lum / 125.0))
        px[x, y] = (int(55 + 200 * t), int(2 + 10 * t), int(2 + 8 * t))
  im.save(dest, quality=85, optimize=True)


if __name__ == "__main__":
  if not NATURAL.exists():
    raise SystemExit(f"missing {NATURAL}")
  recolor(NATURAL, OUT)
  print(f"wrote {OUT}")
