"""
Media Module
Handles media control commands.
"""

from media_control import (
    play_pause,
    next_track,
    previous_track,
    volume_up,
    volume_down,
    mute,
    unmute,
)


def handle(cmd: str):

    if "play" in cmd or "pause" in cmd:
        return play_pause()

    elif "next song" in cmd or "next track" in cmd:
        return next_track()

    elif "previous song" in cmd or "previous track" in cmd:
        return previous_track()

    elif "volume up" in cmd:
        return volume_up()

    elif "volume down" in cmd:
        return volume_down()

    elif "mute" in cmd:
        return mute()

    elif "unmute" in cmd:
        return unmute()

    return None