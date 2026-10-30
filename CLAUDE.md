# ChimeIn Agent

Personal Playwright agent: during a class time window it watches ChimeIn, detects new free-text
questions, drafts a short answer with Claude, and submits it. The owner is learning — explain each
change in plain language and build one roadmap step at a time (see README.md).

## Stack
- Python 3.13, virtualenv in `.venv/` (run tools via `.venv/Scripts/python`)
- Playwright **sync** API, Chromium
- Anthropic SDK for answers; config from `.env` via python-dotenv
- SQLite for seen-question state; Python `logging` for logs
- Production target: small Linux cloud server, scheduled 9:05–10:00 local class time

## Rules
- Never read, print, or commit `.env` or anything in `auth/` (saved login session = password-equivalent).
- Never automate the ChimeIn/SSO login itself; the owner logs in by hand and we save the session.
- Prefer role/text selectors (`get_by_role`, `get_by_text`) over CSS classes.
- Every failure path logs, saves a screenshot, and keeps running if it safely can.
- Keep code simple and readable over clever; small modules, no frameworks.
