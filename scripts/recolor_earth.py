#!/usr/bin/env python3
"""Bake black/red/white Earth texture from assets/earth-map-natural.jpg.

Oceans -> near-black with subtle grey depth, land -> red, ice/clouds -> white.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
NATURAL = ROOT / "assets" / "earth-map-natural.jpg"
OUT = ROOT / "assets" / "earth-map.jpg"


def luminance(r, g, b):
  return 0.299 * r + 0.587 * g + 0.114 * b


def is_ice_or_cloud(r, g, b):
  # Bright + low saturation: polar ice / clouds (must win over ocean detect).
  lum = luminance(r, g, b)
  mx, mn = max(r, g, b), min(r, g, b)
  sat = ((mx - mn) / mx) if mx else 0
  if lum >= 150 and sat < 0.28:
    return True
  if lum >= 175 and sat < 0.38:
    return True
  return False


def is_ocean(r, g, b):
  if b > r + 4 and b > g + 2:
    return True
  if b >= g and b > r and b < 90 and r < 70:
    return True
  return False


def ocean_pixel(x, y, r, g, b):
  # Subtle neutral grey depth — quieter than the last pass.
  water = max(b, luminance(r, g, b))
  depth = max(0.0, min(1.0, (water - 20) / 110.0))
  grain = ((x * 37 + y * 17) % 9) - 4  # -4..4
  v = int(10 + 30 * depth + grain)
  v = max(8, min(42, v))
  return (v, v, v)


def recolor(src: Path, dest: Path) -> None:
  im = Image.open(src).convert("RGB")
  px = im.load()
  w, h = im.size
  for y in range(h):
    for x in range(w):
      r, g, b = px[x, y]
      lum = luminance(r, g, b)
      if is_ice_or_cloud(r, g, b):
        # Keep poles/clouds white (with a little brightness from source)
        t = max(0.0, min(1.0, (lum - 140) / 90.0))
        v = int(220 + 35 * t)
        px[x, y] = (v, v, v)
      elif is_ocean(r, g, b):
        px[x, y] = ocean_pixel(x, y, r, g, b)
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
