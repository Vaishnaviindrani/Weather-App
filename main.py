from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BASE_URL = "http://api.weatherstack.com/current"
API_KEY = "340a2e5e329d3f682d87057f978e3fd1"  # Replace with your Weatherstack API key

def get_weather(city):
    params = {
        "access_key": API_KEY,
        "query": city
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "success" in data and not data["success"]:
            return {"error": data["error"]["info"]}
        if "current" in data:
            return {
                "temperature": data["current"].get("temperature", "N/A"),
                "condition": data["current"].get("weather_descriptions", ["N/A"])[0],
                "wind_speed": data["current"].get("wind_speed", "N/A"),
                "humidity": data["current"].get("humidity", "N/A")
            }
    return {"error": "Error fetching data. Check API key and connection."}

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather(city)
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
