import os
import requests
from math import floor
from datetime import datetime
from speaker import speaker
from platform import system
from AppOpener import open


def greeter(info):
    current = datetime.now()
    state_of_day = None
    if float(current.strftime('%H.%M')) <= 12.00:
        state_of_day = "Good Morning"

    elif 12.00 <= float(current.strftime('%H.%M')) <= 16.00:
        state_of_day = "Good Afternoon"

    elif float(current.strftime('%H.%M')) > 16.00:
        state_of_day = "Good Evening"

    statement = f"{state_of_day} {info[0]}"
    print(statement + '!')
    speaker(statement + ', How can I help you today?')


def helper():
    speaker("here are my commands")
    print("Command list:\n"
        "['helper'             : reveive a list of all the commands]----------------------[short-command: 'h']\n"
        "['time'               : get the current time]------------------------------------[short-command: 't']\n"
        "['weather'            : receive the weather data of your specified city]---------[short-command: 'w']\n"
        "['joke'               : receive a random joke]-----------------------------------[short-command: 'j']\n"
        "['config'             : edit your user info]-------------------------------------[short-command: 'c']\n"
        "['open-app={app-name}': command to open a specified app]-------------------------[short-command: 'o-a' or 'oa'+var]\n"
        "['exit'               : exit jarpy]----------------------------------------------[short-command: 'e']"
        )


def current_time():
    current = datetime.now()
    print(f"Date: {str(current.strftime('%d %B %Y'))}\nCurrent time: {str(current.strftime('%I:%M %p'))}")
    speaker(f"Today is {str(current.strftime('%d %B %Y'))} and the current time is" + str(current.strftime('%I:%M %p')))


def weather(location):
    # ================================================================================ #
    # =============================== Weather Map API ================================ #
    # ================================================================================ #

    # Accessing the data through API
    speaker('Fetching weather information...')
    with open('/Users/Shared/userinfo.txt', 'r') as n:
        updated_info = n.read()
        info = updated_info.split(';')
        api_key = info[3]

    location = location
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()

        # Check for successful response
        if response.status_code == 200:
            # variables to store data on
            temperature = floor(data["main"]["temp"] - 273.15)
            feels_like = floor(data['main']['feels_like'] - 273.15)
            temp_min = floor(data['main']['temp_min'] - 273.15)
            temp_max = floor(data['main']['temp_max'] - 273.15)
            humidity = floor(data['main']['humidity'])
            pressure = data['main']['pressure']
            # weather_condition = data['weather']['description']
            wind_speed = data['wind']['speed']

            draft = f'''The current temperature at {location} is {temperature}degree celsius.
                But it feels like {feels_like}℃. The minimum temperature is {temp_min}℃ and the maximum is {temp_max}℃. 
                The humidity is {humidity} percent and the pressure is {pressure}. 
                The wind speed is {wind_speed}. 
                So plan the day accordingly. Have a Good day.'''

            print(
                f'''Current temperature at {location}: {temperature}℃\n
                But it feels like: {feels_like}℃\n
                Minimum temp: {temp_min}℃/ Maximum temp: {temp_max}℃\n
                Humidity: {humidity}%| Pressure: {pressure}| 
                Wind speed: {wind_speed}''')

            speaker(draft)

        
        else:
            print(f"Error: {response.status_code}")

    
    except requests.exceptions.ConnectionError:
        print("Error: Can't connect.")
        speaker("Sorry, can't retrieve weather data, please check your internet connection.")



def jokes():
    # ======================================================================== #
    # =============================== JokeAPI ================================ #
    # ======================================================================== #
    speaker('Crunching the funniest joke...')
    # Getting data through API
    url = f"https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()
    
    if data['type'] == 'twopart':
        if 'setup' in data:
            text = data['setup']
            print(text)
            speaker(text)
        text = data['delivery']
        print(text)
        speaker(text)
        speaker('I hope you find it funny')

    
    elif data['type'] == 'single':
        if 'setup' in data:
            text = data['setup']
            print(text)
            speaker(text)
            speaker('I hope you find it funny')


def app_opener(app_name):
    # ================================================================================================= #
    # =========================== For macOS =========================================================== #
    # ================================================================================================= #

    # ===========================Defining app list for common ones in macOS============================ #
    app_white_list = {'gimp':'GIMP.app',
                    'vs code':"Visual\ Studio\ Code.app",
                    'code':"Visual\ Studio\ Code.app",
                    }
    # ================================================================================================= #
    if app_name  == 'ls':
        speaker('Here are all the apps available for launch')
        print('User applications')
        for app in os.listdir('/Applications'): print('\t',app) 
        print('System applications')
        for app in os.listdir('/system/Applications'): print('\t',app)
        speaker("Name the app to launch")
        app_name = input('Name the app to launch : ')
        app_opener(app_name)

    
    elif app_name in app_white_list:
        os.system("open /Applications/"+app_white_list[app_name])

    
    else :
        app_name = app_name.replace(' ','\ ')
        os.system("open /System/Applications/"+app_name+".app")
        os.system("open /Applications/"+app_name+".app")


def maintenance_tasks():
    # ================================================================================================= #
    # =========================== For routine maintenance Tasks ======================================= #
    # ================================================================================================= #
    if system() == 'Darwin':
        os.chdir('~/Library/Caches')
        print(os.getcwd())

    
    elif system() == 'Linux':
        pass

    
    elif system() == 'Windows':
        pass
