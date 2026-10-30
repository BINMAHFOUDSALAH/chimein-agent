"""Step 2: log in to ChimeIn by hand once and save the session.

Run:  .venv\\Scripts\\python login.py

A browser window opens. Log in yourself (SSO, Duo, etc.), open your class,
then come back to this terminal and press Enter. Your session is saved to
auth/state.json so the agent can reuse it without your password.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

CHIMEIN_URL = os.getenv("CHIMEIN_URL", "https://chimein.cla.umn.edu")
STATE_FILE = Path("auth/state.json")


def main():
    STATE_FILE.parent.mkdir(exist_ok=True)

    with sync_playwright() as p:
        # headless=False shows a real window so you can log in by hand.
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(CHIMEIN_URL)

        input("\nLog in in the browser window, open your class, then press Enter here... ")

        # Saves cookies + local storage (your logged-in session) to a file.
        context.storage_state(path=STATE_FILE)
        print(f"Session saved to {STATE_FILE}. Keep this file private, it works like a password.")

        browser.close()


if __name__ == "__main__":
    main()
