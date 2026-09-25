# Open-Meteo API Example
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=56.946&longitude=24.1059&hourly=temperature_2m,rain&timezone=auto"
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url)
data = response.json()


res = requests.get("https://geocoding-api.open-meteo.com/v1/search?name=Riga&count=1", timeout=20)
res.raise_for_status()
print(res.json())


city_long
city_lat
city_name