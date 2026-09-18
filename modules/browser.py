"""
Browser Module
Handles browser-related commands.
"""

from commands import (
    open_google,
    open_youtube,
    open_github,
    open_chatgpt,
    
)
from automation import open_chrome

def handle(cmd: str):

    if "open google" in cmd:
        open_google()
        return "Opening Google."

    elif "open youtube" in cmd:
        open_youtube()
        return "Opening YouTube."

    elif "open github" in cmd:
        open_github()
        return "Opening GitHub."

    elif "open chatgpt" in cmd:
        open_chatgpt()
        return "Opening ChatGPT."

    elif "open chrome" in cmd:
        return open_chrome()

    return None