import os
from PIL import Image
import json
import webbrowser


SignDictionary = {
    'A': r'C:\Users\HP\Desktop\Code\Hands\A.jpeg',
    'B': r'C:\Users\HP\Desktop\Code\Hands\B.jpeg',
    'C': r'C:\Users\HP\Desktop\Code\Hands\C.jpeg',
    'D': r'C:\Users\HP\Desktop\Code\Hands\D.jpeg',
    'E': r'C:\Users\HP\Desktop\Code\Hands\E.jpeg',
    'F': r'C:\Users\HP\Desktop\Code\Hands\F.jpeg',
    'G': r'C:\Users\HP\Desktop\Code\Hands\G.jpeg',
    'H': r'C:\Users\HP\Desktop\Code\Hands\H.jpeg',
    'I': r'C:\Users\HP\Desktop\Code\Hands\I.jpeg',
    'J': r'C:\Users\HP\Desktop\Code\Hands\J.jpeg',
    'K': r'C:\Users\HP\Desktop\Code\Hands\K.jpeg',
    'L': r'C:\Users\HP\Desktop\Code\Hands\L.jpeg',
    'M': r'C:\Users\HP\Desktop\Code\Hands\M.jpeg',
    'N': r'C:\Users\HP\Desktop\Code\Hands\N.jpeg',
    'O': r'C:\Users\HP\Desktop\Code\Hands\O.jpeg',
    'P': r'C:\Users\HP\Desktop\Code\Hands\P.jpeg',
    'Q': r'C:\Users\HP\Desktop\Code\Hands\Q.jpeg',
    'R': r'C:\Users\HP\Desktop\Code\Hands\R.jpeg',
    'S': r'C:\Users\HP\Desktop\Code\Hands\S.jpeg',
    'T': r'C:\Users\HP\Desktop\Code\Hands\T.jpeg',
    'U': r'C:\Users\HP\Desktop\Code\Hands\U.jpeg',
    'V': r'C:\Users\HP\Desktop\Code\Hands\V.jpeg',
    'W': r'C:\Users\HP\Desktop\Code\Hands\W.jpeg',
    'X': r'C:\Users\HP\Desktop\Code\Hands\X.jpeg',
    'Y': r'C:\Users\HP\Desktop\Code\Hands\Y.jpeg',
    'Z': r'C:\Users\HP\Desktop\Code\Hands\Z.jpeg',
    '1': r'C:\Users\HP\Desktop\Code\Hands\1.jpeg',
    '2': r'C:\Users\HP\Desktop\Code\Hands\2.jpeg',
    '3': r'C:\Users\HP\Desktop\Code\Hands\3.jpeg',
    '4': r'C:\Users\HP\Desktop\Code\Hands\4.jpeg',
    '5': r'C:\Users\HP\Desktop\Code\Hands\5.jpeg',
    '6': r'C:\Users\HP\Desktop\Code\Hands\6.jpeg',
    '7': r'C:\Users\HP\Desktop\Code\Hands\7.jpeg',
    '8': r'C:\Users\HP\Desktop\Code\Hands\8.jpeg',
    '9': r'C:\Users\HP\Desktop\Code\Hands\9.jpeg',
    '0': r'C:\Users\HP\Desktop\Code\Hands\0.jpeg'
}
with open("WLASL_v0.3.json", 'r') as data:
    sign_data = json.load(data)

def  GetSignVideo(text):
    for enter in sign_data:
        if enter['gloss'].upper() == text.upper():
            if "instances" in enter and enter["instances"]:
                return enter["instances"][0]["url"]
    return None

def PlayVideo(sent):
    texts = sent.upper().split()
    for text in texts:
        video_url = GetSignVideo(text)
        if video_url:
            webbrowser.open(video_url)
        else:
            print(f"No sign video found for the word {text}.")

def TextToSign(text):
    text = text.upper()
    images = []
    for ch in text:
        if ch in SignDictionary:
            img = Image.open(SignDictionary[ch])
            img.show()
            images.append(img)
    return images

text = input("Input text: ").upper()

if len(text) <2:
    TextToSign(text)
else:
    PlayVideo(text)