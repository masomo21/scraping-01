import requests
import json


def fetch_weather_data():
    """
    Fetch the maximum temperature forecast for Tokyo using the Open-Meteo API.

    Returns:
        dict: A dictionary containing the date and the maximum temperature.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 35.6895,
        "longitude": 139.6917,
        "daily": "temperature_2m_max",
        "timezone": "Asia/Tokyo",
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    daily = response.json()["daily"]
    return {
        "date": daily["time"][0],
        "max_temperature": daily["temperature_2m_max"][0],
    }


def save_to_json(data, filename):
    """
    Save the extracted weather data to a JSON file.

    Args:
        data (dict): The data to be saved.
        filename (str): The name of the JSON file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    # Fetch the weather data
    weather_data = fetch_weather_data()

    # Save the data to a JSON file
    save_to_json(weather_data, "tokyo_weather.json")

    print("Data successfully saved to tokyo_weather.json")
