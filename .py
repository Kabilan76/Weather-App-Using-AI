import requests

# OpenWeatherMap API key (Replace with your API key)
API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# AI-Based Recommendation Function
def get_weather_recommendation(weather, temp):
    if "rain" in weather.lower():
        return "It's rainy! Don't forget your umbrella ☔."
    elif "clear" in weather.lower():
        return "The sky is clear! A great day to go out 🌞."
    elif "cloud" in weather.lower():
        return "It's cloudy! Might be a bit dull ☁."
    elif temp < 10:
        return "It's quite cold! Wear warm clothes ❄️."
    elif temp > 30:
        return "It's hot! Stay hydrated 🥵."
    else:
        return "Weather looks fine! Have a nice day 😊."

# Function to Get Weather Data
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"\n🌍 City: {city}")
        print(f"🌡 Temperature: {temp}°C")
        print(f"🌦 Weather: {weather.capitalize()}")
        print(f"💡 AI Suggestion: {get_weather_recommendation(weather, temp)}")
    else:
        print("❌ City not found. Please enter a valid city name.")

# Run the App
city_name = input("Enter city name: ")
get_weather(city_name)
