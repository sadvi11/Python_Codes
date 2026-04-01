import requests
import json

# 1. CALL a free public API (no login needed)
url = "https://api.open-meteo.com/v1/forecast?latitude=51.05&longitude=-114.07&current_weather=true"

response = requests.get(url)

# 2. CHECK if it worked
print("Status code:", response.status_code)  # 200 = success

# 3. CONVERT response to Python dictionary
data = response.json()

# 4. USE the data
weather = data["current_weather"]
print(f"Temperature in Calgary: {weather['temperature']}°C")
print(f"Wind speed: {weather['windspeed']} km/h")

# 5. SAVE it to a JSON file
with open("weather_report.json", "w") as f:
    json.dump(data, f, indent=4)
    print("Saved to weather_report.json!")