import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

joke_api_url = 'https://v2.jokeapi.dev/joke/Any'
joke_api_key = 'YOUR_JOKEAPI_KEY'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause = 1
        audio = r.listen(source)
    try:
        print('Recongnizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'You said: {query}\n')
    except Exception as e:
        print(e)
        speak('I didnt understand. Please try again.')
        return None
    return query
def get_weather(city):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        speak(f"The weather in {city} is {weather_description} with a temperature of {temperature} degrees Celsius.")
    else:
        speak("Sorry, I couldn't fetch the weather information at the moment.")

def get_joke():
    headers = {
        'accept': 'application/json',
    }
    params = {
        'apiKey': joke_api_key,
    }

    response = requests.get(joke_api_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'single':
            joke = data['joke']
        else:
            joke = f"{data['setup']} {data['delivery']}"
        speak(joke)
    else:
        speak("Sorry, I couldn't fetch a joke at the moment.")
    
def shutdown_computer():
    speak("Shutting down the computer.")
    os.system("shutdown /s /t 1") 

def restart_computer():
    speak("Restarting the computer.")
    os.system("shutdown /r /t 1")

def lock_computer():
    speak("Locking the computer.")
    os.system("rundll32.exe user32.dll,LockWorkStation") 

if __name__ == '__main__':
    speak("Hi, I'm Violet. Nice to meet you.")
    speak('How can I help you ?')
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching for result')
            query = query.replace('wikipedia','')
            results =wikipedia.summary(query,sentences = 4)
            speak('According to Wikipedia')
            speak(results)
        elif 'are you' in query:
            speak('I am Violet. An Simple voice search AI. Verion 1.1. Created and developed by Sagnick Mondal')
        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open('google.com')
        elif 'open bing' in query:
            speak('Opening bing')
            webbrowser.open('bing.com')
        elif 'open spotify' in query:
            speak('Opening spotify')
            webbrowser.open('spotify.com')
        elif 'open github' in query:
            speak('Opening gihub')
            webbrowser.open('github.com')
        elif 'open gmail' in query:
            speak('Opening gmail')
            webbrowser.open('gmail.com')
        elif 'open chatgpt' in query:
            speak('Opening chatgpt')
            webbrowser.open('chat.openai.com')
        elif 'open twitch' in query:
            speak('Opening twitch tv')
            webbrowser.open('twitch.tv')
        elif 'twitter' in query:
            speak('Opening twitter')
            webbrowser.open('twitter.com')
        elif 'search' in query:
            speak(f'searching for {query}')
            query = query.replace('search','')
            results =wikipedia.summary(query,sentences = 4)
            speak('According to Wikipedia')
            speak(results)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'weather' in query:
            speak('Sure, which city would you like the weather for?')
            city = take_command()
            get_weather(city)
        elif 'tell me a joke' in query:
            get_joke()
        elif 'Nice' or 'good' or 'great' in query:
            speak('thank you')
        if 'shutdown' in query:
            shutdown_computer()
        elif 'restart' in query:
            restart_computer()
        elif 'lock' in query:
            lock_computer()
        elif 'sleep' or 'bye' or 'goodbye' or 'stop' in query:
            speak('Hope I have helped you. Bye')
            exit(0)
        


