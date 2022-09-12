import json
import pyttsx3
import speech_recognition as sr
import datetime


r = sr.Recognizer()
machine = pyttsx3.init()
json_open = open("commands.json", encoding='utf-8')
commands = json.load(json_open)
time = datetime.datetime.now()
time_t = time.strftime("%H:%M")

data_space = commands['nasa']['space image']
data_hours = commands['date and hour']['hours']
data_temperature = commands['weather']['temperature']

data_lofi = commands['music']['lofi']
data_music1 = commands['music']['music1']
data_music2 = commands['music']['music2']
data_music3 = commands['music']['music3']
data_music4 = commands['music']['music4']

data_wiki = commands['search']['wikipedia']
data_google = commands['search']['google']
data_youtube = commands['search']['youtube']

try:
    with sr.Microphone() as source:
        audio = r.listen(source)
        spc = str(r.recognize_google(audio, language='pt-BR'))
        print(spc)
except:
    pass
