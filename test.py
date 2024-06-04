import requests
from math import floor

url = f"https://api.oceandrivers.com/static/resources.json"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(data)