import pyttsx3

def TextToSpeach(text):
    SpeachEngine = pyttsx3.init()
    SpeachEngine.setProperty('rate', 150)
    SpeachEngine.setProperty('volume', 1.0)

    SpeachEngine.say(text)
    SpeachEngine.runAndWait()

