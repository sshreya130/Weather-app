import requests

API_KEY = "API key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()

    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print("Weather:", weather)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind, "m/s")

else:
    print("Error:", response.status_code)
    print(response.json())
