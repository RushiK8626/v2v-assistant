from dotenv import load_dotenv
import os
from groq import Groq
from gtts import gTTS
import tempfile

load_dotenv()

groqClient = Groq(api_key=os.environ["GROQ_API_KEY"])

def speech_to_text(filename):
    with open(filename, "rb") as file:
        transcription = groqClient.audio.transcriptions.create(
            file=(filename, file.read()),
            model="whisper-large-v3-turbo",
            response_format="json",  
            temperature=0.0           
        )
    return transcription.text

def text_to_speech(text):
    tts = gTTS(text=text, lang="en", tld="co.in")

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    tts.save(temp_file.name)

    return temp_file.name