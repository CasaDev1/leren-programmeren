import requests

APP_ID = 'a352db877902bafba7d0ed23e7660331'
url = 'https://api.openweathermap.org/data/2.5/weather?q=Dordrecht&appid=' + APP_ID
response = requests.get(url)

json_response = response.json()
wind_speed = json_response['main']['temp']


print(f" in Dordrecht is de tempratuur {wind_speed}K")
