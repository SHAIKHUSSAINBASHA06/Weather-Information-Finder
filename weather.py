import requests

api_key = '75c74429676dd5396adae7fad84f9a29'

user_input = input("Enter city name:")

weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}')

if weather_data.json()['cod'] == '404':
    print("City not found. Please check the city name and try again.")

else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])  

    print(f"The weather in {user_input} is : {weather} ")
    print(f"The temperature in {user_input} is : {temp}°F")