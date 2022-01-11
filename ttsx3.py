import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
lis = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')


engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    while command =='':
        try:
            with sr.Microphone() as so:
                print("listening...")
                voice = lis.listen(so)
                command = (lis.recognize_google(voice)).lower()
                print(command)
                if 'alexa' in command:
                    command = command.replace('alexa','')
                    print(command)
        except:
            pass
    return command
def run_alx():
    co = take_command()

    if 'play' in co:
        song = co.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    else:
        talk('please say the command again')
while True:
    run_alx()
