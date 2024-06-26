import pyttsx3
import datetime
import speech_recognition as lr
import wikipedia
import webbrowser
import os
import pyautogui
from googletrans import Translator
mydic={
    "Debanjan":" ",
    "Monimala": " ",
    "Srija":" ",
    "sanjana":" ",
    "Gadai": " ",
    "sarkar":" ",
    "Atanu":" ",
    "Abhijit":" "


}

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)




def speak (audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good moring ")
    elif hour>=12 and hour<=16:
        speak("Good afternoon")
    elif hour>=16 and hour<=19:
        speak("Good evening")
    else:
        speak("Good night sweet dreams")
 
    

def takecommand():
    r=lr.Recognizer()
    with lr.Microphone() as source :
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)

        print("Say that again please...")
        return "None"
    return query

#def sendEmail(mydic,content):




if __name__=="__main__":
    wish()
    while(True):
        query= takecommand().lower()

        if 'wikipedia' in query :
            speak('searching wikipedia.....')
            query= query. replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        elif 'linkdin' in query:
            webbrowser.open("linkdin.com")
        

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")
        elif "open" in query :
            query=query.replace("open","")
            query=query.replace("jarvis","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif 'open  code' in query:
            codepath="C:\\Users\\ABHIJIT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)
        
        '''elif 'email to debanjan' in query:
            try:
                speak("What should i say?")
                content=takecommand()
                sendEmail=(mydic,content)
                speak("Email has been sent")'''
            

        


        
        
    


    

    
