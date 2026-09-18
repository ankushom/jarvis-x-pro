"""
Vision Module
Handles camera and screen vision commands.
"""

from camera_ai import analyze_camera
from screen_vision import analyze_screen
from screen_ai import capture_screen


def handle(cmd: str):

    cmd = cmd.lower().strip()

    if (
        "analyze screen" in cmd
        or "analyze my screen" in cmd
        or "what is on my screen" in cmd
        or "screen vision" in cmd
    ):

        print(">>> VISION MODULE: SCREEN ANALYSIS <<<")

        image_path = capture_screen()

        if not image_path:
            return "Sorry Sir, I couldn't capture the screen."

        return analyze_screen(image_path)

    elif (
        "analyze camera" in cmd
        or "what do you see" in cmd
        or "what can you see" in cmd
        or "look around" in cmd
        or "look at me" in cmd
        or "camera vision" in cmd
    ):

        print(">>> VISION MODULE: CAMERA ANALYSIS <<<")

        return analyze_camera()

    return None
