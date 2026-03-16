import requests # type: ignore

API_KEY = "849850f06e7cf93647a7430cd6c82e65"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]



    print("\nWeather Details")
    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Weather:", weather)
    print("Humidity:", humidity, "%")

else:
    print("City not found")