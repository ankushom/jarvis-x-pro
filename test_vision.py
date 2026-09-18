from modules.vision import handle

commands = [
    "camera",
    "analyze camera",
    "vision"
]

for cmd in commands:
    print("----------------------")
    print("Command:", cmd)
    print("Result:", handle(cmd))