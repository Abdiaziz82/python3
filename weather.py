import requests

lat = -0.447170
lon = 39.659850
API_KEY = "68482b2f329c4291cfc0a06e15a7364c"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    country = data['sys']['country']
    county_name = data['name']
    
    print(f"the temperature is {temperature} degrees")
    print(f"the humidity is {humidity} %")
    print(f"the description is {description}")
    print(f"the country is {country} ")
    print(f"the county name is {county_name}")
    
else:
    print(f"{response.status_code}")
    