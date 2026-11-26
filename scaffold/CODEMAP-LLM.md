# Code map (agent reference)

Dense codebase/system map for agents — compact is fine. Optimized so an agent can understand the system without grepping the whole codebase.

Confirmed product and system facts only. No open questions. Lessons and pitfalls belong here as short factual notes, or in scaffold/CODEMAP-HUMAN.md when they are mainly a maintainer-facing map note.

## Product

- Site: Instagram-link destination for **Good Power Infinity** — a living transmission (feel it and leave; no ask).
- Brand on page: **Good Power Infinity** (hero).
- Seal on page: **Good Power Infinity, So that Evil May Be a Solved Problem, Inc.**
- Byline: **By Jd Diamari** (same gap below seal as seal has below brand).
- Ticker under Earth: **$GPI 5T** (bright green; playful market-cap signal).
- Earth grade: black / red / white baked into `assets/earth-map.jpg` via `scripts/recolor_earth.py` from `assets/earth-map-natural.jpg` (CSS blend tint is not used — it failed to show real red on the spinning sphere).
- No product cards, no manifesto scroll of founder letter, no ritual/portal, no forms/CTAs/mailto.
- Ambition (brief, not page copy): coalition factory / creation machine; keep the good in power forever; civilization-scale; aims the world at the good future.
- Founder “I am alive…” letter is creative brief only — not page copy.

## Stack

- Static HTML/CSS/JS. Preview: `python3 -m http.server 5173` from repo root.
- Earth beside title: CSS sphere + `assets/earth-map.jpg` (map scrolls horizontally).
- Tests: `python3 -m unittest tests.test_page -v`
