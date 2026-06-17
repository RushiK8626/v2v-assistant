import sounddevice as sd
from scipy.io.wavfile import write

duration = 5 
sample_rate = 16000

def record_audio(filename="question.wav"):
    print("Speak now...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, sample_rate, audio)