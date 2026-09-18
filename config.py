"""
Jarvis X Pro Configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# APP
# ==========================

APP_NAME = "Jarvis X Pro"

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 950

# ==========================
# THEME
# ==========================

BACKGROUND = "#1e1e1e"
PANEL = "#2b2b2b"
ACCENT = "#00d4ff"

# ==========================
# AI
# ==========================

AI_NAME = "Jarvis"

# ==========================
# GEMINI
# ==========================

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing from .env")

SYSTEM_PROMPT = """
You are Jarvis X Pro.

You are a highly intelligent desktop AI assistant.

Rules:

- Reply naturally.
- Keep answers concise unless more detail is requested.
- Help with coding.
- Help with Windows.
- Help with automation.
- Never invent facts.
- If you don't know something, say so.
- Be polite and professional.
"""

# ==========================
# VOICE
# ==========================

VOICE_RATE = 175
VOICE_VOLUME = 1.0

# ==========================
# WHISPER
# ==========================

WHISPER_MODEL = "base"

SAMPLE_RATE = 16000

RECORD_SECONDS = 5
