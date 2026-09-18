import asyncio
import edge_tts
import tempfile
import os
import threading
from playsound import playsound

VOICE = "en-IN-NeerjaNeural"

_lock = threading.Lock()


async def _generate(text, filename):

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save(filename)


def speak(text: str):

    if not text.strip():
        return

    print("🔊 Jarvis:", text)

    with _lock:

        fd, filename = tempfile.mkstemp(suffix=".mp3")

        os.close(fd)

        try:

            asyncio.run(
                _generate(text, filename)
            )

            playsound(filename)

        finally:

            if os.path.exists(filename):

                os.remove(filename)


def stop():
    pass