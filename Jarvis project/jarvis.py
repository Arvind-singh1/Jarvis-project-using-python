import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
 # print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour<=12 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening! Sir.")
    speak("I am your assistant , Sir tell me how may i help you")
def takeCommand():
    #IT takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query =r.recognize_google(audio,Language='en-In')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print("say that again please....")
        return "None"
    return query
if __name__=="__main__":
    wishMe()
    takeCommand()
    #speak("Arvind is a good boy")
    while True:
        query=takeCommand().lower()

        #logic for execution task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")
        elif 'open google' in query:
            webbrowser.open("Google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        #elif 'play music' in query:
            music_dir='D:\\Songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is  {strTime}")
        #elif 'open code' in query:
            codepath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft vs Code\\Code.exe"
            os.startfile(codepath)
