import tkinter as tk
from tkinter import scrolledtext
import datetime
import webbrowser

def send_command():

```
command = entry.get().lower()

chat.insert(tk.END, "\nYou: " + command + "\n")

if command == "hello":
    response = "Hello Rudraksh!"

elif command == "time":
    response = datetime.datetime.now().strftime(
        "Current Time: %H:%M:%S"
    )

elif command == "date":
    response = str(datetime.date.today())

elif command == "google":
    webbrowser.open("https://google.com")
    response = "Opening Google"

elif command == "youtube":
    webbrowser.open("https://youtube.com")
    response = "Opening YouTube"

elif command == "exit":
    root.destroy()
    return

else:
    response = "Command not found"

chat.insert(tk.END, "Jarvis: " + response + "\n")

entry.delete(0, tk.END)
```

# ==========================

# GUI WINDOW

# ==========================

root = tk.Tk()

root.title("Jarvis AI Assistant")
root.geometry("700x500")

title = tk.Label(
root,
text="JARVIS AI ASSISTANT",
font=("Arial", 18, "bold")
)

title.pack(pady=10)

chat = scrolledtext.ScrolledText(
root,
width=80,
height=20
)

chat.pack(pady=10)

entry = tk.Entry(
root,
width=50,
font=("Arial", 12)
)

entry.pack(pady=10)

send_button = tk.Button(
root,
text="Send",
command=send_command
)

send_button.pack()

root.mainloop()
