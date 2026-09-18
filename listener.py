import tempfile
import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel

model = None


def get_model():
    global model

    if model is None:
        print("Loading Whisper Model...")
        model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    return model


def listen(duration=5):

    sample_rate = 16000

    print("🎤 Listening...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:

        sf.write(f.name, audio, sample_rate)

        model = get_model()

        segments, info = model.transcribe(f.name)

    text = "".join(segment.text for segment in segments).strip()

    print("You:", text)

    return text