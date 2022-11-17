import requests

API_KEY = "" #past your API Key
BASE_URL = "" #past URL 

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}@q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.115,2)
    
    print("Weather:", weather)
    print("Temperature: ", temperature, "celsius")
else:
    print("error occured.")