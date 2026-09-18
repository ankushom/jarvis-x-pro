"""
Vision Module
Handles camera and screen vision commands.
"""

from camera_ai import analyze_camera
from screen_vision import analyze_screen
from screen_ai import capture_screen


def handle(cmd: str):

    cmd = cmd.lower().strip()

    if "analyze screen" in cmd:

        image_path = capture_screen()

        if not image_path:
            return "Sorry Sir, I couldn't capture the screen."

        return analyze_screen(image_path)

    elif "analyze camera" in cmd:
        return analyze_camera()

    elif cmd == "camera":
        return analyze_camera()

    return None