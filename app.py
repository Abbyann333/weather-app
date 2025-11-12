import requests

API_KEY = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
city = input("Enter city: Canton ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

response = requests.get(url)
data = response.json()

print(f"Weather in {city}: {data['weather'][0]['description']}, Temp: {data['main']['temp']}°F")
