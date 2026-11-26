#!/usr/bin/env python3
"""Bake black/red/white Earth texture from assets/earth-map-natural.jpg."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
NATURAL = ROOT / "assets" / "earth-map-natural.jpg"
OUT = ROOT / "assets" / "earth-map.jpg"


def recolor(src: Path, dest: Path) -> None:
  im = Image.open(src).convert("RGB")
  px = im.load()
  w, h = im.size
  for y in range(h):
    for x in range(w):
      r, g, b = px[x, y]
      lum = 0.299 * r + 0.587 * g + 0.114 * b
      ocean = b > r + 12 and b > g + 8 and b > 70
      if ocean:
        px[x, y] = (0, 0, 0)
      elif lum >= 200:
        px[x, y] = (245, 245, 245)
      elif lum >= 165:
        t = (lum - 165) / 35.0
        px[x, y] = (int(210 + 45 * t), int(24 + 210 * t), int(24 + 210 * t))
      else:
        t = max(0.28, min(1.0, lum / 130.0))
        px[x, y] = (int(48 + 195 * t), int(2 + 12 * t), int(2 + 10 * t))
  im.save(dest, quality=85, optimize=True)


if __name__ == "__main__":
  if not NATURAL.exists():
    raise SystemExit(f"missing {NATURAL}")
  recolor(NATURAL, OUT)
  print(f"wrote {OUT}")
