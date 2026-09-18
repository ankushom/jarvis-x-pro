import pyautogui


def capture_screen():

    path = "screen_capture.png"

    screenshot = pyautogui.screenshot()

    screenshot.save(path)

    return path