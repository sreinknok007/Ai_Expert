import threading
import sys

try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import speech_recognition as sr
    from speech_recognition import AudioData
except ImportError as e:
    print(f"Missing library: {e.name}")
    print("? Install commands:")
    print(" Windows: pip install SpeechRecognition pyaudio numpy matplotlib")
    print(" macOS: brew install portaudio && pip install SpeechRecognition pyaudio numpy matplotlib")