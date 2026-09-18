from modules.desktop import handle

commands = [
    "open notepad",
    "open calculator"
]

for cmd in commands:
    print("----------------------")
    print("Command:", cmd)
    print("Result:", handle(cmd))