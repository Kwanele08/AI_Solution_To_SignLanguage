import pyttsx3

def TextToSpeech(text):
    SpeachEngine = pyttsx3.init()
    SpeachEngine.setProperty('rate', 150)
    SpeachEngine.setProperty('volume', 1.0)

    SpeachEngine.say(text)
    SpeachEngine.runAndWait()

text = 'Hello, My name is Bob'
TextToSpeech(text)