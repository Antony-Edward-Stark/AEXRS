from speaker import speaker
import requests
try:
    list = ['https://saurav.tech/NewsAPI/top-headlines/category/health/in.json',
            'https://saurav.tech/NewsAPI/top-headlines/category/science/in.json',
            'https://saurav.tech/NewsAPI/top-headlines/category/general/in.json',
            ]
    for item in list:
        url = item
        response = requests.get(url)
        data = response.json()
        data = data['articles']
        for i in data:
            print(i['title'],'\n',i['description'])
except requests.exceptions.ConnectionError:
            print("Error: Can't connect. Check Internet")
            speaker("Sorry, can't retrieve weather data, please check your internet connection.")