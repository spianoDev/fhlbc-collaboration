import pandas as pd
import requests
import emoji
from termcolor import colored
from tabulate import tabulate

# Set up API key and base URL
api_key = '5c65f5efbe41769f1bbf62c86e8f9b07'
base_url = 'http://api.openweathermap.org/data/2.5/weather'

# Set up a dictionary of cities and their coordinates
cities = {
    'Atlanta': (33.749, -84.388),
    'Boston': (42.361, -71.058),
    'Chicago': (41.878, -87.629),
    'Cincinnati': (39.103, -84.512),
    'Dallas': (32.776, -96.797),
    'Des Moines': (41.591, -93.603),
    'Indianapolis': (39.768, -86.158),
    'New York': (40.712, -74.006),
    'Pittsburgh': (40.441, -79.996),
    'San Francisco': (37.774, -122.419),
    'Seattle': (47.606, -122.332),
    'Topeka': (39.048, -95.677)
}

# Set up an empty dataframe to hold the weather data
weather_data = pd.DataFrame(columns=['city','temperature', 'weather', 'mood'])

# Loop through the cities and retrieve their weather data
for city, coordinates in cities.items():
    latitude, longitude = coordinates
    query_params = {'lat': latitude, 'lon': longitude, 'appid': api_key, 'units': 'imperial'}
    response = requests.get(base_url, params=query_params)
    if response.ok:
        data = response.json()
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']

        # Set the mood emoji based on temperature
        if temperature > 70:
            mood = emoji.emojize(':hot_face:')
        elif temperature > 60:
            mood = emoji.emojize(':smiling_face_with_sunglasses:')
        elif temperature > 50:
            mood = emoji.emojize(':slightly_smiling_face:')
        else:
            mood = emoji.emojize(':cold_face:')

        color = 'blue' if temperature < 50 else 'red' if temperature > 70 else 'yellow'
        temperature_text = colored(f'{temperature:.1f}°F', color)
        city_weather_data = pd.DataFrame([[city, temperature_text, weather, mood]], columns=['city', 'temperature', 'weather', 'mood'])
        weather_data = pd.concat([weather_data, city_weather_data], ignore_index=True)
    else:
        print(f"Error retrieving weather data for {city}")

# Set up the formatting for the printed output
tablefmt = 'fancy_grid'
headers = weather_data.columns.tolist()
table_data = weather_data.values.tolist()

# Print the resulting dataframe with borders
print(tabulate(table_data, headers=headers, tablefmt=tablefmt))
