import requests

API_KEY = '42b531b9d9bdd45125650e05a5faf633' 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    ("DEBUG URL:", url)  # ✅ Show the full request URL
    ("DEBUG STATUS:", response.status_code)  # ✅ See what status we got
    ("DEBUG RESPONSE:", response.text)  # ✅ Full response content
    
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        return temp, condition
    else:
        return None, None


def suggest_clothes(temp):
    if temp is None:
        return "❌ Couldn’t fetch weather. Try again."
    if temp > 30:
        return "🩳 It's hot! Wear light cotton clothes."
    elif 20 < temp <= 30:
        return "👕 Warm weather — t-shirt and jeans are perfect."
    elif 10 < temp <= 20:
        return "🧥 It's cool. A light jacket would be nice."
    else:
        return "🧣 Brrr... it's cold! Wear warm clothes and a jacket."

# --- Main ---
city = input("🌍 Enter a city name: ")
temp, condition = get_weather(city)

if temp is not None:
    print(f"\n📍 {city.title()}")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"🌦️ Weather: {condition}")
    print(f"👚 Clothing Suggestion: {suggest_clothes(temp)}")
else:
    print("⚠️ Couldn't find the city or fetch data.")
