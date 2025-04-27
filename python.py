import requests

def get_weather(city):
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == "404":
        return f"Error: {data['message']}"
    
    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"]
    }
    
    return weather

print(get_weather("New York"))
