import random
import sys
import os , subprocess
import speech_recognition as sr
import pyttsx3
import datetime
import cv2
import random
from requests import get
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)
engine.setProperty("rate", 350)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Didn't catch that. Say that again please...")
        return none
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning Aditi, how can I help you?")
    elif hour >= 12 and hour < 17:
        speak("Good afternoon Aditi, how can I help you?")
    else:
        speak("Good evening Aditi, how can I help you?")

# def search_google(query):
#     browser = webdriver.Safari()
#     browser.get('http://www.google.com')
#     search = browser.find_element_by_name('q')
#     search.send_keys(query)
#     search.send_keys(Keys.RETURN)



if __name__ == "__main__":
    wish()
    while True:
    # if 1:
        query = listen().lower()
        if "open Twitter" in query:
            os.system("open /Applications/Twitter.app")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while (True):
                ret, frame = cap.read()
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
                cv2.imshow('frame', rgb)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    out = cv2.imwrite('capture.jpg', frame)
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "/Users/aditiagarwal/Desktop/music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            subprocess.call(["open", os.path.join(music_dir, rd)])

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        # elif 'search google for ' in query:
        #     speak("Searching...")
        #     search_google(query)

        elif 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Aditi, what do you want me to search on YouTube")
            command = listen().lower()
            kit.playonyt(command)

        elif 'search google for ' in query:
            command = query[18:]
            speak(f"Searching google for {command}")
            kit.search(command)

        elif 'send whatsapp message' in query:
            speak("Tell me the number you want me to whatsapp to: ")
            number = listen().lower()
            kit.sendwhatmsg(number, "testing", 18, 14)

        elif 'no' in query:
            speak("Okay then, bye Aditi")
            sys.exit()

        speak('Do you want me to do anything else for you?')

