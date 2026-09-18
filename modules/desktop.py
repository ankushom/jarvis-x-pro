"""
Desktop Module
Handles desktop application commands.
"""
from commands import (
    open_notepad,
    open_calculator,
)



def handle(cmd: str):

    if "open notepad" in cmd:
        open_notepad()
        return "Opening Notepad."

    elif "open calculator" in cmd:
        open_calculator()
        return "Opening Calculator."

    

    return None