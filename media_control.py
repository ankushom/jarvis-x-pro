import pyautogui


def play_pause():
    pyautogui.press("playpause")
    return "Playing or pausing media."


def next_track():
    pyautogui.press("nexttrack")
    return "Playing the next track."


def previous_track():
    pyautogui.press("prevtrack")
    return "Playing the previous track."


def volume_up():
    pyautogui.press("volumeup")
    return "Increasing the volume."


def volume_down():
    pyautogui.press("volumedown")
    return "Decreasing the volume."


def mute():
    pyautogui.press("volumemute")
    return "Muting the volume."


def unmute():
    pyautogui.press("volumemute")
    return "Unmuting the volume."