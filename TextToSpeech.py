import pyttsx3

def TextToSpeech(text):
    SpeechEngine = pyttsx3.init()
    SpeechEngine.setProperty('rate', 150)
    SpeechEngine.setProperty('volume', 1.0)

    SpeechEngine.say(text)
    SpeechEngine.runAndWait()

