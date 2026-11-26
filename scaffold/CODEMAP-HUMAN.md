# Code map

Map of this project's codebase for the maintainer: which files do what, how data and control flow between them, where state lives. Prefer diagrams (mermaid or ASCII). Write in the first person (I, me, my).

## What belongs here

- File / module map: important paths and one-line roles
- Data and control flow between those pieces
- Where state lives (DB, files, env, memory, external services)
- Diagrams of the above when they clarify the map

## What does not belong here

- Install, run, or usage instructions — those live in root `README.md` (keep that README lean)
- Product pitch or "what this app is for" — durable product/system facts go in `scaffold/CODEMAP-LLM.md`
- Generic tutorials, glossaries, or coaching

## Layout

```
index.html          # the page: brand + seal
css/styles.css      # atmosphere, type, motion
js/main.js          # marks body live after paint
tests/test_page.py  # brand/seal present; no CTA; no banned taglines
```

## Flow

```mermaid
flowchart LR
  Browser --> index.html
  index.html --> stylesCss[css/styles.css]
  index.html --> mainJs[js/main.js]
```

## State

- None. Static files only; no database, env secrets, or server-side state.
