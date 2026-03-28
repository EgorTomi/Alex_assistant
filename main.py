import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import subprocess
import os
import pyttsx3
import sintez 
import time
import requests

def Ai_responce(text: str) -> str:
    API_KEY = "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"  # ключ OpenRouter


    url = "https://openrouter.ai/api/v1/chat/completions"



    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        # необязательно:
        # "HTTP-Referer": "https://your-site.com",
        # "X-Title": "My Test Bot",
    }

    data = {
        "model": "openrouter/free",
        "messages": [
            {"role": "system", "content": "Ты полезный помощник, который кратно отвечает на вопросы и запросы, может рассказать что то и тд на русском языке."},
            {f"role": "user", "content": text}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        answer = result["choices"][0]["message"]["content"]
       # print(result["choices"][0]["message"]["content"])
        print("Какая модель ответила:", result.get("model"))
        print("Ответ ИИ:", answer)
        return answer

    except requests.exceptions.HTTPError:
        print("HTTP ошибка:", response.status_code)
        print(response.text)

    except requests.exceptions.RequestException as e:
        print("Ошибка запроса:", e)

    except KeyError:
        print("Неожиданный формат ответа:")
        print(response.text)


engine = pyttsx3.init() # object creation
# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
print(voices)
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for femal


duration = 5 #длительность записи в секундах
sampel_rate = 44100 #частота дискретизации
language = 'ru-RU' #язык распознавания
url = "https://roadmap.sh/"
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

print("говорите...")
engine.say("Слушаю")
engine.runAndWait()
while True:    
    recording = sd.rec(int(duration* sampel_rate), samplerate=sampel_rate, channels=1, dtype='int16')
    sd.wait()

    wav.write('output.wav', sampel_rate, recording)
    print("запись завершена, идет распознавание...")
    engine.say("Распознаю")
    time.sleep(2)
    engine.runAndWait()

    recognizer = sr.Recognizer()
    with sr.AudioFile('output.wav') as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language=language)
        print("Вы сказали: " + text)
        if "Открой Steam" in str(text) or "открой Steam" in str(text):
            engine.say("Открываю Steam")
            time.sleep(1.5)
            engine.runAndWait()
            os.startfile(r'C:/Program Files (x86)/Steam/steam.exe')

        elif "Открой браузер" in str(text) or "открой браузер" in str(text):
            engine.say("Открываю браузер")
            time.sleep(1.5)
            engine.runAndWait()
            os.startfile(chrome_path)

        elif "открой roadmap" in str(text) or "Открой roadmap" in str(text) or "Открой Road Map" in str(text) or "открой Road Map" in str(text):
            os.system(f'"{chrome_path}" {url}')
            engine.say("Открываю Road Map")
            engine.runAndWait()

        elif "завершить" in str(text) or "Завершить" in str(text):
            print("Программа завершена")
            engine.say("Понял, завершаю программу")
            time.sleep(3)
            engine.runAndWait()
            break

        else:
            ai_answer = Ai_responce(str(text))
            if ai_answer:
                engine.say(ai_answer)
                time.sleep(60)
                engine.runAndWait()

            else:
                engine.say("Не получил ответ от ИИ")
                engine.runAndWait()

    except Exception as e:
        print("Распознавание не удалось", e)
        engine.say("Распознавание не удалось")
        time.sleep(2.5)
        engine.runAndWait()
            

