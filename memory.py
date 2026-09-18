"""
Jarvis X Pro
Memory Module
"""

import json
import os

MEMORY_FILE = "memory.json"

DEFAULT_MEMORY = {
    "user": {},
    "preferences": {},
    "history": []
}


def load_memory():

    if not os.path.exists(MEMORY_FILE):

        save_memory(DEFAULT_MEMORY)

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:

        return json.load(file)


def save_memory(data):

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def remember(key, value):

    data = load_memory()

    data["user"][key] = value

    save_memory(data)


def recall(key):

    data = load_memory()

    return data["user"].get(key)


def add_history(role, message):

    data = load_memory()

    data["history"].append({
        "role": role,
        "message": message
    })

    # Keep last 100 messages only
    data["history"] = data["history"][-100:]

    save_memory(data)


def get_history():

    return load_memory()["history"]


def clear_history():

    data = load_memory()

    data["history"] = []

    save_memory(data)