#from curses import has_extended_color_support
from os import environ
import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr 
from random import choice
from utils import opening_text
import pyaudio
import requests
from functions.online_ops import *
from functions.os_ops import *
from pprint import pprint
import subprocess as sp
from ecapture import ecapture as ec


USERNAME=config('USER')
BOTNAME= config("BOTNAME")

engine = pyttsx3.init('sapi5')

#setting rate
engine.setProperty('rate', 180)
#setting volume
voices= engine.getProperty('voices')
engine.setProperty('volume', 1.0)
engine.setProperty('voice', voices[1].id)


#text to speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

# speak( "hello , how can i help you ... ")

def greet_user():
    hour = datetime.now().hour
    print(hour)
    if (hour > 6) and (hour < 12):
        speak(f"Good morning  {USERNAME}")
    
    elif (hour >= 12) and (hour < 17):
        speak(f"Good Afternoon {USERNAME}")

    elif (hour >= 17) and (hour < 19):
        speak(f"Good Evening  {USERNAME}")
    else :
        speak("it's late sir you should sleep now ! ")
    speak(f"I am {BOTNAME}. How may I assist you?")
    #speak("i will kick abhinandan's ass for free sir  ")

def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source)
        audio =r.listen(source)

        try:
            print('Recognizing.....')
            query=r.recognize_google(audio , language='en-in')
            print(query)
            if  'sleep' in query or 'exit' in query or 'goodbye' in query :
                # speak(choice(opening_text))
                hour = datetime.now().hour
                if (hour>=21)and (hour < 6 ):
                    speak ('Good Night . Take care sir ')
                else:
                    speak("I am logging off sir ! ")
                    speak('Have a good day sir!')
                exit()
        except Exception: 
            speak('Sorry, I could not understand. Could you please say that again?')
            query = 'None'
    return query
if __name__ == '__main__':
    greet_user()
    while True:
        query= take_user_input().lower()

        
        if 'open notepad' in query or 'start notepad' in query :
            open_notepad()
            
        elif 'open command prompt' in query or ' open CMD' in query :
            open_cmd()

        elif 'open zoom' in query or 'start zoom' in query:
            open_zoom()

        elif 'open excel' in query or 'start excel' in query :
            open_excel()

        elif 'open powerpoint' in query or 'start powerpoint' in query:
            open_point()
        
        elif  "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")
            continue
            

        elif 'open word' in query or 'start word' in query:
            open_word()

        elif "open vlc" in query or "start vlc" in query:
            open_vlc()
            
        elif 'open camera' in query or 'start camera' in query:
            open_camera()
        
        elif 'open calculator 'in query or 'start calculator 'in query:
            open_calculator()
            
        elif 'ip address' in query :
            ip_address= find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f"your IP Address is {ip_address}")
            
                
        elif 'youtube' in query:
            speak("what do i play on youtube ????")
            video = take_user_input().lower
            play_on_youtube(video)
            
        elif 'search on google' in query :
            speak("what do i search for , sir ")
            query= take_user_input().lower()
            search_on_google(query)

        
            
        elif "send a whatsapp message" in query or "send Whatsapp " in query  :
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whataspp_msg(number, message)
            speak("Message sent .")
            
        elif "send email" in query:
            speak("who is the reciepint !  Please enter in the console: ")
            receiver_address = input("Enter email address: ")                
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            if receiver_address== "me":
                receiver_address= {EMAIL}
                print(receiver_address)
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("Email sent")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs .")
                
                
        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)


        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
            
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(f"{BOTNAME}")
            print(f"My friends call me",  {BOTNAME})
            
        elif "who made you" in query or "who created you" in query:
            speak(f"I have been created by {USERNAME}")
            
        elif "who i am" in query:
            speak("If you talk then definitely you are a  human.")
            
      
            
        elif 'what can you do' in query :
            speak("sir , i can send whatsapp messages,emails , open programs like notepad, cmd, calculator and search information on web ! ")
            speak("also ! here is a list of tasks i can perform on the consooe sir  ")
            print("sir , i can send whatsapp messages,emails ,\n open programs like notepad, cmd, \n calculator and search information on web !\n try sepaking these commands ")
            take_user_input()
        
        elif "log off" in query or "shut down" in query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                print("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                sp.call(["shutdown", "/l"])

        elif 'wikipedia' in query:
            speak('What do you want to search on wikipedia , sir ?')
            search_query = take_user_input().lower()
            results = search_in_wikipedia(search_query)
            speak(f"According to Wikipedia , {results}")
            speak("For your convenince , i am printing it on the sir ")
            print(results)






