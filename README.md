## Weather report: A Python Weather & Clothing Suggestion App

# Project Overview

Welcome to Weather report, my 4th project in the 100 Days of Coding challenge! This Python app uses the OpenWeatherMap API to fetch real-time weather data for any city and suggests appropriate clothing based on the temperature. It’s a simple, fun, and practical tool to help you dress for the day!

# Features





 Weather Lookup: Enter a city name to get the current temperature (in Celsius) and weather condition.



 Clothing Suggestions: Get emoji-powered outfit ideas based on temperature ranges:





 - 30°C: Light cotton clothes 🩳



- 20–30°C: T-shirt and jeans 👕



- 10–20°C: Light jacket 🧥



- ≤ 10°C: Warm clothes and jacket 🧣



 Debug Mode: Prints the API URL, status code, and response for easy troubleshooting.



 User-Friendly: Simple input and clear output with emojis for a fun touch.

# Tech Stack





 Language: Python 3



 Library: requests for API calls



 API: OpenWeatherMap (free tier)



 Key Concepts: API integration, HTTP requests, JSON parsing, conditional logic

# How It Works





- Enter a city name.



- The app queries the OpenWeatherMap API for weather data.



- It extracts the temperature and condition.



- Based on the temperature, it suggests what to wear.



- Debug info (URL, status, response) helps track issues.

 Setup

 Prerequisites





- Python 3 installed



- requests library: pip install requests



- An OpenWeatherMap API key (sign up at openweathermap.org)

# Installation





 - Clone this repo:

git clone https://github.comkaiisherebbg/weather-report.git



 - Navigate to the project:

cd weather-report



 - Install dependencies:

pip install requests



 - Replace the API_KEY in the code with your own from OpenWeatherMap:

API_KEY = 'your-api-key-here'



 - Run the script:

python weather_report.py

# Usage





- Run the script and enter a city (e.g., "London").



- See the temperature, weather, and a clothing suggestion.



# Example output:

🌍 Enter a city name: dehradun
 DEBUG URL: https://api.openweathermap.org/data/2.5/weather?q=London&appid=your-api-key&units=metric
 

 DEBUG STATUS: 200

 
 DEBUG RESPONSE: {"main":{"temp":15.2},"weather":[{"description":"cloudy"}]...}

- 📍 dehradun
- 🌡️ Temperature: 15.2°C
- 🌦️ Weather: cloudy
- 👚 Clothing Suggestion: 🧥 It's cool. A light jacket would be nice.

# Limitations





- Requires a valid API key and internet connection.



- Basic error handling; invalid cities return a simple error message.



- Temperature-based suggestions are simplified (no wind, humidity, etc.).

# Future Improvements





- Add support for Fahrenheit units.



- Include more weather factors (e.g., rain, wind) for better suggestions.



- Save favorite cities for quick lookup.



- Add a GUI for a better user experience.

# Learning Outcomes





- Mastered API integration with requests.



- Practiced parsing JSON responses.



- Improved logic for conditional statements.



- Gained experience with real-world data and error handling.

# Acknowledgments





Thanks to OpenWeatherMap for the free API.💗



 Part of my 100 Days of Coding journey—day 4 of 100!

# License

 MIT License—feel free to use, modify, and share!
