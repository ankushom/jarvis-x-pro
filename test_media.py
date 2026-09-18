from modules.media import handle

commands = [
    "play",
    "next track",
    "previous track",
    "volume up",
    "volume down",
    "mute",
    "unmute"
]

for cmd in commands:
    print("-----------------------")
    print("Command:", cmd)
    print("Result:", handle(cmd))