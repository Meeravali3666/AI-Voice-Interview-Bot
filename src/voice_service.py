import pyttsx3
import speech_recognition as sr

def speak_text(text):
    """
    Converts text to speech.

    Args:
        text (str): The text to be spoken.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    engine.say(text)
    engine.runAndWait()

def record_audio():
    """
    Records audio from the microphone and converts it to text.

    Returns:
        str: Recognized text or None if recognition failed.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError:
            print("Speech recognition service unavailable.")
            return None
