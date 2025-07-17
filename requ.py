import requests

lat = -0.452862
lon = 39.661255
API_KEY = "68482b2f329c4291cfc0a06e15a7364c"

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
response = requests.get(url)
data = response.json()

print(f"Location: {data['name']}")
print(f"Temperature: {data['main']['temp']}°C")
print(f"Weather: {data['weather'][0]['description']}")