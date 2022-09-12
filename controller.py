import main
from APIs.weather_api import temp, temperature
from APIs.nasa_api import imgtoday
import wikipedia
from playsound import playsound

try:
    def exec():
        # hours command
        if main.spc == main.data_hours:
            main.machine.say(main.time_t)
            main.machine.runAndWait()

        # musics commands
        elif main.spc == main.data_music1:
            print('playing "De Kenner" - LEOD')
            playsound.playsound(r'./sounds/music/de_kenner.mp3')
        elif main.spc == main.data_music2:
            print('playing "Poze indie" - LEOD')
            playsound.playsound(r'./sounds/music/poze_indie.mp3')
        elif main.spc == main.data_music3:
            print('playing "Hotline chique" - LEOD')
            playsound.playsound(r'./sounds/music/HOTLINE_MUSIC.mp3')
        elif main.spc == main.data_music4:
            print('playing "Se ta solteira" - LEOD')
            playsound.playsound(r'./sounds/music/SE_TA_SOLTEIRA.mp3')
        elif main.spc == main.data_lofi:
            print('Playing LOFI compilation')
            playsound.playsound(r'./sounds/music/lofi.mp3')

        # temperature command
        elif main.data_temperature in main.spc:
            temperature()
            
        # search youtube command
        elif main.data_youtube in main.spc:
            search_youtube = main.spc.replace('Maria Pesquise por', '')
            link = f'https://www.youtube.com/results?search_query={search_youtube}'
            main.webbrowser.open(link)

        # search google command
        elif main.data_google in main.spc:
            search_google = main.spc.replace('Maria busque por', '')
            link = f'https://www.google.com/search?q={search_google}'
            main.webbrowser.open(link)

        # search wikipedia command
        elif main.data_wiki in main.spc:
            search = main.spc.replace('Maria procure por', '')
            wikipedia.set_lang('pt')
            result = wikipedia.summary(search, 2)
            link = "wikipedia.org/wiki/"
            main.webbrowser.open(link + search)
            main.machine.say(result)
            main.machine.runAndWait()
            
        # space image command
        elif main.spc == main.data_space:
            imgtoday()
except:
    pass
