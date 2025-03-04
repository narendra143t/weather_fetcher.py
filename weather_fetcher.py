import requests

API_KEY = "891fe485bfb957a6ee40e018bf9200cf"  # Replace with your OpenWeatherMap API key
CITY = "Chennai"
BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(BASE_URL)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"Current Temperature in {CITY}: {temp}°C")
    print(f"Weather: {weather}")
else:
    print("Error fetching weather data")
