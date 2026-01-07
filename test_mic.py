import sounddevice as sd
import queue
from vosk import Model, KaldiRecognizer
import json

# Load model
model = Model("model")
recognizer = KaldiRecognizer(model, 16000)

# Create queue to store audio chunks
audio_queue = queue.Queue()

# Callback: runs every time new audio arrives
def callback(indata, frames, time, status):
    if status:
        print("Status:", status)
    audio_queue.put(bytes(indata))

print("🎤 Starting microphone test...")
print("Speak something... (Ctrl+C to stop)\n")

# Start audio stream
with sd.RawInputStream(samplerate=16000,
                       blocksize=8000,
                       dtype="int16",
                       channels=1,
                       callback=callback):

    while True:
        data = audio_queue.get()
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            if result.get("text"):
                print("You said:", result["text"])
        else:
            partial = json.loads(recognizer.PartialResult())
            # print("Partial:", partial["partial"])  # Optional: live text
