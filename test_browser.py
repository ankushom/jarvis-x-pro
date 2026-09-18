from modules.browser import handle

commands = [
    "open google",
    "open youtube",
    "open github",
    "open chatgpt",
    "open chrome"
]

for cmd in commands:
    print("--------------------------------")
    print("Command:", cmd)

    result = handle(cmd)

    print("Result:", result)