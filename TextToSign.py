from PIL import Image
import requests
from io import BytesIO
import json
import webbrowser

SignDictionary = {
    'A': 'https://drive.google.com/uc?id=1ASu81_jbjs-8XkGDsi6nGLrO5lFD6xfs',
    'B': 'https://drive.google.com/uc?id=1uGLrz2io8BLGrmk4dSeeRAMGShwh3Nk1',
    'C': 'https://drive.google.com/uc?id=1f7sMg5VXjlDlrzlmQ9xYEoYY-60gMekH',
    'D': 'https://drive.google.com/uc?id=1Xg6zbXbZmFVx3cT1o6fgsDjri3hQwd2F',
    'E': 'https://drive.google.com/uc?id=1-_yYpb52KfK5B1ZypNGl5e9QicNxZa3S',
    'F': 'https://drive.google.com/uc?id=1oBNlmeh5RxEjjkED4TYiv7DzMDeN8pq9',
    'G': 'https://drive.google.com/uc?id=1M9Zdh1faFcBa0LmKRucZjTyN49YwJAJb',
    'H': 'https://drive.google.com/uc?id=1F28VE29E8H6caPrMsn-ZfpaAcoH3fAul',
    'I': 'https://drive.google.com/uc?id=1cNfdUT9y-DE9W2vqKBy-vagu2ahcU3WN',
    'J': 'https://drive.google.com/uc?id=1T-LhkGNIQJU9rJoVq-EmhSsCQ2HrQlP3',
    'K': 'https://drive.google.com/uc?id=1LWkCnGITlszqU_G6Kt3jogJzpdr0fxud',
    'L': 'https://drive.google.com/uc?id=1rusESEuAA0oBW3fxugFvGv_p1x0flRGY',
    'M': 'https://drive.google.com/uc?id=1prZhsXDdyX0gncQ-S9vXZNZHbZH5n4pf',
    'N': 'https://drive.google.com/uc?id=1AvUpPLAgwwsnWcJggGRToAarMXLfC9y6',
    'O': 'https://drive.google.com/uc?id=1kABRYHrR6yayLvK_nBKviKkSGFDlOKL_',
    'P': 'https://drive.google.com/uc?id=1wei8L0m6HHNkSaoy_SbkyqN1ffZrgqbn',
    'Q': 'https://drive.google.com/uc?id=1cp8bbk65lkHOwZNbwo-36PvfPvagqviH',
    'R': 'https://drive.google.com/uc?id=1dpZHQmnIG9hoXlhM077ZviQ0RusRaN6n',
    'S': 'https://drive.google.com/uc?id=1BAWofYLRO27J1AnpVtx3tfwngjU2MPk-',
    'T': 'https://drive.google.com/uc?id=1hhc93QuqoSzLhPTAQ1Y6yIym4uh65XR7',
    'U': 'https://drive.google.com/uc?id=1UQrmR3kd6iTKIWVHFZMqBfLjhJsdiOx3',
    'V': 'https://drive.google.com/uc?id=1MOtYFAkVVRdD7iwjIcsaAb5aG9T8epE2',
    'W': 'https://drive.google.com/uc?id=1fWn623L_Spog1WAHsaozMKRwy8LYGPC4',
    'X': 'https://drive.google.com/uc?id=12_2BuwIp2fmXyLqxHoNudG_XRVzNrThq',
    'Y': 'https://drive.google.com/uc?id=1H70QDqfBjZ64FS94unSEbB2GJlGaxMLx',
    'Z': 'https://drive.google.com/uc?id=1Stlm2cEiguSPlRrbOH7iMHikSCUv74yi',
    '1': 'https://drive.google.com/uc?id=14UQDIjJ2OWjevS3RJYmcx7_QVrANDOpJ',
    '2': 'https://drive.google.com/uc?id=1S_PzFdYKCSXx4zBX3tVPwZgclGcdlmzB',
    '3': 'https://drive.google.com/uc?id=10UYAaftb7YoJak1yOvrowigoCTU8l5_n',
    '4': 'https://drive.google.com/uc?id=1XGTMJQPh7-B3Mz-nQJlTfVym_roYJP5D',
    '5': 'https://drive.google.com/uc?id=1rbM-zjGoSJxYTuw6ei60Wf_lTh8YpO-2',
    '6': 'https://drive.google.com/uc?id=1ibT4JFjxUQ2AerM_4vhQswQEU_jqDE5_',
    '7': 'https://drive.google.com/uc?id=1APqY65T3Tx_A03nGSevw1Z3amztGOVY7',
    '8': 'https://drive.google.com/uc?id=11yRKxAEgsVE-Rrx6B_e12gBy6DAG65ki',
    '9': 'https://drive.google.com/uc?id=1dZdB7ocf02YYFiLCR3kn9MVJ_kGHYapi',
    '0': 'https://drive.google.com/uc?id=1dHzVJUafGVfWQHRAUT7D4WNJmHxUc80M'
}



with open("WLASL_v0.3.json", 'r', encoding='utf-8') as data:
    sign_data = json.load(data)


def GetSignVideos(text):
    videos = []
    for entry in sign_data:
        if entry['gloss'].strip().lower() == text.strip().lower():
            if "instances" in entry and entry["instances"]:
                videos.extend([instance["url"] for instance in entry["instances"] if "url" in instance])
    return videos if videos else None

def PlayVideos(sent):
    texts = sent.upper().split()
    for text in texts:
        video_urls = GetSignVideos(text)
        if video_urls:
            for url in video_urls:
                webbrowser.open(url)
        else:
            print(f"Sorry, no sign video found for the word '{text}'.")


def TextToSign(text):
    text = text.upper()
    images = []
    for ch in text:
        if ch in SignDictionary:
            img_url = SignDictionary[ch]
            print(f"Attempting to fetch image from URL: {img_url}")  # Debugging line
            response = requests.get(img_url)

            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                img.show()
                images.append(img)
            else:
                print(f"Failed to retrieve image for {ch}. HTTP status code: {response.status_code}")

    return images

text = input("Input text: ").upper()

if len(text) < 2:
    TextToSign(text)
else:
    PlayVideos(text)
