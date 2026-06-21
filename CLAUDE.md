# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the project

```bash
python main.py
```

The project uses a `.venv` virtual environment. Activate it before running:

```bash
# Windows
.venv\Scripts\activate
```

## Architecture

This is a small Python scripting project with no external dependencies beyond the standard library.

- `main.py` — entry point; runs all demos and prints output to stdout
- `football.py` — module containing two lookup functions:
  - `get_football_club_by_ranking(ranking)` — returns a club name for ranks 1–49
  - `get_uk_university_by_ranking(ranking)` — returns a university name for ranks 1–100

Both functions use 1-based indexing and return an error string (not an exception) when the ranking is out of range.

New features follow the same pattern: define lookup functions in a separate module, import them into `main.py`, and call them there.

This is a learning project. I'm a beginner learning Python.
- Always explain your changes and the reasoning behind them.
- Prefer simple, readable code over clever or advanced code.
- When I have a bug, walk me through *why* it happened, not just the fix.