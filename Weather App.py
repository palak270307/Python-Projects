import requests

API_KEY = "12df24494f2795d19536f8f286d9d3d1"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

choice = input("Enter 'city' or 'lat_long': ").strip().lower()

if choice == "city":
    city_name = input("Enter the city name: ").strip()
    country_code = input("Enter the country code: ").strip().capitalize()
    complete_url = f"{BASE_URL}?q={city_name},{country_code}&appid={API_KEY}&units=metric"

elif choice == "lat_long":
    lat = input("Enter the latitude: ").strip()
    long = input("Enter the longitude: ").strip()
    complete_url = f"{BASE_URL}?lat={lat}&lon={long}&appid={API_KEY}&units=metric"

else:
    print("Invalid choice! Exiting...")
    exit()

response = requests.get(complete_url)

if response.status_code == 200:
    data = response.json()

    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]       # Correct key
    humidity = data["main"]["humidity"]
    windspeed = data["wind"]["speed"]
    city_name = data["name"]

    print(f"\nCity: {city_name}")
    print(f"Weather Description: {weather_description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {windspeed} m/s")

else:
    print("Error: City/coordinates not found or API request failed.")
