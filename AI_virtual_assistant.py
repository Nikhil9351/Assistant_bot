import pyttsx3
import speech_recognition as sr
import datetime as dt
import webbrowser
import os
import wikipedia

name="friday"  #name of the assistant

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)
#(voices [0].id)          #two voice models voice[0] and[1]
engine.setProperty('voice', voices [1].id)
r = sr.Recognizer()

def speak(s):           #method for speaking
    engine.say(s)
    engine.runAndWait()


def keyword():        #method to trigger the assistant
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold=3000
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            key = r.recognize_google(audio, language='en-in')
            print(key)
            return name in key.lower()
        except Exception:
            keyword()

def takeCommand():        #method to take commands
    if keyword():
        print("...")
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            #r.pause_threshold=1
            audio1 = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio1, language='en-in')
                print(query)
                return query
            except Exception:
                print("cant understand ¯\_(ツ)_/¯ , say that again please")
                speak("i cannot understand that , say that again please")
                return"none"
    else:
        return "none"


hour = int(dt.datetime.now().hour)
if 0 <= hour < 12:
    speak("Good Morning!")
elif 12 <= hour < 18:
    speak("Good Afternoon!")
else:
    speak("Good Evening!")
speak("my name is "+name+" and i am your virtual assistant, how may I help you")

while True:
    cmd = takeCommand().lower()
    if 'none' in cmd:
        print("")
    elif 'open google' in cmd:
        webbrowser.open("https://www.google.com")
    elif 'open youtube' in cmd:
        webbrowser.open("https://www.youtube.com")
    elif 'open facebook' in cmd:
        webbrowser.open("https://www.facebook.com")
    elif 'open instagram' in cmd:
        webbrowser.open("https://www.instagram.com")
    elif 'open wikipedia' in cmd:
        webbrowser.open("https://www.wikipedia.com")
    elif 'open'and'in browser'and'.com'in cmd:
        cmd=cmd.replace(" in browser","").replace("open ","").replace(".com","")
        webbrowser.open("http://www."+cmd+".com")


    elif 'time' in cmd:
        strTime = dt.datetime.now().strftime("%I %M %p")
        speak("the time is "+strTime)
        print(strTime)
    elif "today"and'date'and'day' in cmd:
        strDate = dt.datetime.now().strftime("%A %d %b %Y")
        print(strDate)
        speak("today is " + strDate)

    elif 'open whatsapp' in cmd:
        os.startfile("E:\\Documents\\WhatsApp Desktop.lnk")

    elif 'play music' in cmd:
        music = 'E:\\music'
        songs = os.listdir(music)
        print("ヾ(⌐■_■)ノ♪")
        print(songs)
        os.startfile(os.path.join(music, songs[0]))
    elif 'open documents' in cmd:
        os.startfile("E:\\Documents")
    elif 'open pictures' in cmd:
        os.startfile("E:\\Pictures")
    elif 'open downloads'in cmd:
        os.startfile("E:\\Downloads")
    elif 'play videos' in cmd:
        os.startfile("E:\\Videos")

    elif'search'and 'on youtube' in cmd:
        cmd = cmd.replace("search ", "").replace(" on youtube", "")
        print("here's what i found on youtube")
        speak("here's what i found on youtube")
        webbrowser.open("https://youtube.com/search?q=" + cmd)
    elif 'search' and 'on google' in cmd:
        cmd = cmd.replace("search ", "").replace(" on google", "")
        print("here's what i found on google")
        speak("here's what i found on google")
        webbrowser.open("https://google.com/search?q=" + cmd)
    elif 'on wikipedia' in cmd:
        cmd = cmd.replace(" on wikipedia", "").replace("search ","")
        print("searching wikipedia")
        speak("searching wikipedia")
        try:
            results = wikipedia.summary(cmd, sentences=3)
            print("according to wikipedia "+results)
            speak("According to Wikipedia ,"+results)
            speak("click on link to find more")
            print("https://www.wikipedia.com/wiki/"+cmd)
        except Exception:
            print("unable to find cmd on wikipedia try again")

    elif'what'in cmd:
        cmd = cmd.replace('what ','').replace('is ','')
        webbrowser.open("https://google.com/search?q=" + cmd)

    elif 'stop' in cmd:
        print("-----------------------------------------")
        exit()

    elif'what can you do'in cmd:
        print("my name is "+name+" and i am your virtual assistant ."
                                 "i can open your favourite websites,search wikipedia and can play you some music too")
        speak("my name is "+name+" and i am your virtual assistant ."
                                 "i can open your favourite websites,search wikipedia and can play you some music too")
    else:
        cmd=cmd.replace("search ","")
        print("here's what i found on google")
        speak("here's what i found on google")
        webbrowser.open("https://google.com/search?q=" + cmd)
