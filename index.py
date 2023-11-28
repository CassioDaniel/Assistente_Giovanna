from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
from requests import get
from bs4 import BeautifulSoup
import webbrowser as browser
import json

hotword = 'giovana'

def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Aguardando o Comando!")
            audio = microfone.listen(source)
            try:
                trigger = (microfone.recognize_google(audio, language='pt-BR'))
                trigger = trigger.lower()

                if hotword in trigger:
                    print('COMANDO: ', trigger)
                    responde('feedback')
                    executa_comandos(trigger)
                    break

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return trigger


def responde(arquivo):
    playsound('audios/' + arquivo + '.mp3')

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    tts.save('audios/mensagem.mp3')
    print('Giovanna: ', mensagem)
    playsound('audios/mensagem.mp3')

def executa_comandos(trigger):
    if 'noticias' in trigger:
        ultimas_noticias()

    elif 'toca' in trigger and 'farol' in trigger:
        playlists('farol')

    elif 'tempo agora' in trigger:
        previsao_tempo(tempo=True)

    elif 'temperatura' in trigger:
        previsao_tempo(minmax=True)

    else:
        mensagem = trigger.strip(hotword)
        cria_audio(mensagem)
        print('COMANDO INVALIDO!', mensagem)
        responde('comando_invalido')

def ultimas_noticias():
    site = get('http://news.google.com/news/rss?need=pt_br&gl=BR&hl=pt')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:2]:
        mensagem = item.title.text
        cria_audio(mensagem)

def playlists(album):
    if album == 'farol':
        browser.open('https://www.youtube.com/watch?v=Qv-96R_RWiY')

def previsao_tempo(tempo=False, minmax=False):
    site = get('https://api.openweathermap.org/data/2.5/weather?q=sao%20paulo,br&lang=pt&appid=3d103516ed55955af901b808511b7707&units=metric')
    clima = site.json()
    #print(json.dumps(clima, indent=4))
    temperatura=clima['main'] ['temp']
    minima=clima['main'] ['temp_min']
    maxima=clima['main'] ['temp_max']
    descricao=clima['weather'][0]['description']
    if tempo:
        mensagem = f'No momento fazem {temperatura} graus, com: {descricao}'
    if minmax:
        mensagem = f'Minima de {minima}, e maxima de {maxima}'
    cria_audio(mensagem)

def main():
   while True:
        monitora_audio()

main()
