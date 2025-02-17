import requests

API_KEY = "4400fbd4f14c17b8cb80df9af98f7acd"  # Replace with your actual API Key
BASE_URL = "http://api.weatherstack.com/current"  # Correct API endpoint

def get_weather(city):
    params = {
        "access_key": API_KEY,  # Ensure correct key name
        "query": city  # Ensure correct query parameter
    }

    response = requests.get(BASE_URL, params=params)

    print(f"Response Status Code: {response.status_code}")  # Debugging
    print(f"Response Content: {response.text}")  # Debugging

    if response.status_code == 200:
        try:
            data = response.json()
            if "success" in data and not data["success"]:
                print(f"API Error: {data['error']['info']}")
                return

            if "current" in data:
                weather = data["current"]
                print(f"\nWeather in {city.capitalize()}:")
                print(f"Temperature: {weather.get('temperature', 'N/A')}°C")
                print(f"Condition: {weather.get('weather_descriptions', ['N/A'])[0]}")
                print(f"Wind Speed: {weather.get('wind_speed', 'N/A')} km/h")
                print(f"Humidity: {weather.get('humidity', 'N/A')}%\n")
            else:
                print("City not found. Please check the name.")
        except requests.exceptions.JSONDecodeError:
            print("Error decoding JSON. API response might be empty or invalid.")
    else:
        print("Error fetching data. Check API key and internet connection.")

city = input("Enter city name: ")
get_weather(city)
