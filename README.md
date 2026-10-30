# ChimeIn Agent

A personal browser-automation agent that watches a ChimeIn class session during a set time window,
detects new free-text questions, drafts a short answer with an LLM, and submits it.

Built as a learning project for Playwright, scheduling, DOM detection, LLM APIs, and error handling.
Use it only where your instructor has approved automated tools.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
playwright install chromium
copy .env.example .env        # then fill in your values
```

## Security

- Your login session file (`auth/`) and `.env` are never committed — see `.gitignore`.
- Treat the session file like a password: anyone holding it can act as you on ChimeIn.

## Roadmap

1. Project setup
2. Log in once and save the session
3. Reuse the saved session
4. Detect questions
5. Remember seen questions
6. Draft answers with an LLM
7. Submit answers
8. Logging and error handling
9. Deploy to a cloud server on a schedule
