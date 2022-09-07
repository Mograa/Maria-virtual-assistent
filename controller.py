import webbrowser
import main
import wikipedia
import requests as req

try:
    def exec():
        # hours command
        if main.spc == main.data_hours:
            main.machine.say(main.time_t)
            main.machine.runAndWait()

        # musics commands
        elif main.spc == main.data_music1:
            main.playsound.playsound(r'./sounds/music/de_kenner.mp3')
        elif main.spc == main.data_music2:
            main.playsound.playsound(r'./sounds/music/poze_indie.mp3')
        elif main.spc == main.data_music3:
            main.playsound.playsound(r'./sounds/music/HOTLINE_MUSIC.mp3')
        elif main.spc == main.data_music4:
            main.playsound.playsound(r'./sounds/music/SE_TA_SOLTEIRA.mp3')

        # temperature command
        elif main.data_temperature in main.spc:
            search_temp = main.spc.replace('Maria qual é a temperatura em', '')
            API_KEY = 'cb3d4b7abf1326d2ba1520686ee7c8c8'
            city = search_temp
            api_link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
            json_req = req.get(api_link).json()
            temp_city = json_req['main']['temp'] - 273.115
            temp_formatted = f'{temp_city:.0f} Graus'
            main.machine.say(temp_formatted)
            main.machine.runAndWait()

        # search youtube command
        elif main.data_youtube in main.spc:
            search_youtube = main.spc.replace('Maria Pesquise por', '')
            link = f'https://www.youtube.com/results?search_query={search_youtube}'
            webbrowser.open(link)

        # search google command
        elif main.data_google in main.spc:
            search_google = main.spc.replace('Maria busque por', '')
            link = f'https://www.google.com/search?q={search_google}'
            webbrowser.open(link)

        # search wikipedia command
        elif main.data_wiki in main.spc:
            search = main.spc.replace('Maria procure por', '')
            wikipedia.set_lang('pt')
            result = wikipedia.summary(search, 2)
            link = "wikipedia.org/wiki/"
            webbrowser.open(link + search)
            main.machine.say(result)
            main.machine.runAndWait()

        # joke command
        elif main.spc == main.data_joke:
            joke = 'Qual o animal que não vale nada. O javali'
            main.machine.say(joke)
            main.machine.runAndWait()
    exec()
except:
    print('Error in controller archive')
