import os
import requests
from math import floor
from datetime import datetime
from speaker import speaker
from platform import system

os.system('clear')


def greeter():
    current = datetime.now()
    if float(current.strftime('%H.%M')) <= 12.00:
        statement = "Good Morning sir, The current time is " + str(current.strftime('%H:%M') + ' AM')
        print(statement)
        speaker(statement)

    elif 12.00 <= float(current.strftime('%H.%M')) <= 16.00:
        statement = "Good Afternoon sir, The current time is " + current.strftime('%H:%M' + ' PM')
        print(statement)
        speaker(statement)

    elif float(current.strftime('%H.%M')) > 16.00:
        statement = "Good Evening sir, The current time is " + current.strftime('%H:%M' + ' PM')
        print(statement)
        speaker(statement)


def weather():
    # ================================================================================ #
    # =============================== Weather Map API ================================ #
    # ================================================================================ #

    # Accessing the data through API
    speaker('Fetching weather information...')
    api_key = '22e6bc8e2472cf6f002311423db6aa1e'
    location = 'Rajamahendravaram'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
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

        draft = f'''The current temperature at {location} is {temperature} degrees celsius. But it feels like {feels_like} degrees celsius. The minimum temperature is {temp_min} degrees celsius and the maximum is {temp_max} degrees celsius. The humidity is {humidity} percent and the pressure is {pressure}. The wind speed is {wind_speed}. So plan the day accordingly. Have a Good day.'''
        print(draft)
        speaker(draft)
    else:
        print(f"Error: {response.status_code}")


def jokes():
    # ======================================================================== #
    # =============================== JokeAPI ================================ #
    # ======================================================================== #

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
    elif data['type'] == 'single':
        if 'setup' in data:
            text = data['setup']
            print(text)
            speaker(text)


def maintainance_tasks():
    # ========================================================================================= #
    # =========================== For routine maintenance Tasks =============================== #
    # ========================================================================================= #
    if system() == 'Darwin':
        os.chdir('~/Library/Caches')
        print(os.getcwd())
    elif system() == 'Linux':
        pass
    elif system() == 'Windows':
        pass


def app_opener(app_name):
    app_name_mod = app_name + '.app'
    app_name_mod = app_name_mod.capitalize()
    print(app_name_mod)
    os.chdir("/Applications")
    if app_name_mod in os.listdir(os.getcwd()):
        print('App present in directory')
        os.system("open " + app_name_mod)
    elif app_name_mod not in os.listdir(os.getcwd()):
        print("app not present")


if __name__ == '__main__':
    app_opener('GIMP')
