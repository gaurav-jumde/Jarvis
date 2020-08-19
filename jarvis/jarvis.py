import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 

    else:
        speak("Good Evening!")    

    speak("I am jarvis Sir. Please tell me how can i help you")       

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language ="en-in")
        print(f"User said:{query}\n")   

    except Exception as e:
        print(e)  
        print("Say That Again Please.....")
        return "None"       
    return query 
 
    
if __name__ == "__main__":
    #speak("Gaurav is a Good boy")  
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower() 

        if "wikipedia" in query: 
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif "open youtube" in query:
             webbrowser.open("youtube.com")

        elif "open gaurav website" in query:
             webbrowser.open("gaurav-jumde.atwebpages.com")  

        elif "open google" in query:
             webbrowser.open("google.com")        

        elif "play music" in query:
            music_dir = "C:\\Users\\Admin\\Music\\songs\\New folder\\Marathi git"  
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime} ")

        elif "open vs code" in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open chrome" in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
 
        elif "quit" in query:
            quit()  