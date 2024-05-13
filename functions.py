import os
from time import sleep
import requests
from math import floor
from datetime import datetime

##################### Initialize pyttsx3 functions #########################################################

############################################################################################################
os.system('clear')                                                                             

def greeter():
    current = datetime.now()
    if  float(current.strftime('%H.%M')) <= 12.00: 
        os.system('say Good Morning Sir, The time is'+str(current.strftime('%H:%M')) )
        print("The current time is ",current.strftime('%H:%M'))
    elif float(current.strftime('%H.%M')) <= 16.00 and float(current.strftime('%H.%M'))>= 12.00 :
        os.system('say Good Afternoon Sir, The time is'+str(current.strftime('%H:%M')))
        print('The current time is ',current.strftime('%H:%M'))
    elif float(current.strftime('%H.%M')) > 16.00: 
        os.system('say Good Evening Sir, The time is'+str(current.strftime('%H:%M')))
        print("The current time is ",current.strftime('%H:%M'))

def weather():
    
    ########################################################################################################
    ################################ Weather Map API #######################################################
    ########################################################################################################
    
    api_key = '22e6bc8e2472cf6f002311423db6aa1e'
    location = 'Bengaluru'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Check for successful response
    if response.status_code == 200:
        #variables to store data on
        temperature = floor(data["main"]["temp"]-273.15)
        feels_like = floor(data['main']['feels_like'] - 273.15)
        temp_min = floor(data['main']['temp_min'] - 273.15)
        temp_max = floor(data['main']['temp_max'] - 273.15)
        humidity = floor(data['main']['humidity'])
        pressure = data['main']['pressure']
        #weather_condition = data['weather']['description']
        wind_speed = data['wind']['speed']
        
        draft = f'''The current temperature at {location} is {temperature} degrees celsius. But it feels like {feels_like} degrees celsius. The minimum temperature is {temp_min} degrees celsius and the maximum is {temp_max} degrees celsius. The humidity is {humidity} percent and the pressure is {pressure}. The wind speed is {wind_speed}. So plan the day accordingly. Have a Good day.'''
        print(draft)
        os.system('say '+draft)
    else:
        print(f"Error: {response.status_code}")

def jokes():
    ########################################################################################################
    ################################ JokeAPI ###############################################################
    ########################################################################################################
    url = f"https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    response = requests.get(url)
    data = response.json()
    if data['type'] == 'twopart':
        print(data['setup'])
        os.system('say '+data['setup'])
        print(data['delivery'])
        os.system('say '+data['delivery'])
    elif data['type'] == 'single':
        print(data['setup'])
        os.system('say '+data['setup'])
for i in range(10):
    try:
        jokes()
        sleep(7)
        os.system('clear')
        i = i+1
    except KeyError:
        pass
