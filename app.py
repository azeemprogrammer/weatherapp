# Import the required libraries
import requests

# Constants
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to get weather information
def get_weather(city_name):
    # Build the URL with the city name and API key
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract relevant data from the JSON response
        main_data = data['main']
        temperature = main_data['temp']
        humidity = main_data['humidity']
        weather_info = data['weather'][0]['description']

        # Display the weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_info.capitalize()}")
    else:
        print("Could not fetch weather data.")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)
