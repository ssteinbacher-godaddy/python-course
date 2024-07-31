import requests

city = 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=d4a58b6c1e0e4747a83224413241907&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print ('Todays weather in', city, 'is', description, 'and', temp, 'degrees')