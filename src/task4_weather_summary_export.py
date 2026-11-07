import json
import csv

HOT_THRESHOLD = 30   # °C
WIND_THRESHOLD = 15  # km/h


def load_json(filename):
    """
    Load JSON data from a file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: The loaded JSON data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def summarize_weather_data(data):
    """
    Summarize the weather data across all days.

    Args:
        data (list of dict): The daily weather data.

    Returns:
        dict: A summary of the key metrics across all days.
    """
    count = len(data)
    if count == 0:
        return {}
    return {
        "average_max_temp": sum(d["max_temperature"] for d in data) / count,
        "average_min_temp": sum(d["min_temperature"] for d in data) / count,
        "total_precipitation": sum(d["precipitation"] for d in data),
        "average_wind_speed": sum(d["wind_speed"] for d in data) / count,
        "average_humidity": sum(d["humidity"] for d in data) / count,
        "hot_days": sum(1 for d in data if d["max_temperature"] > HOT_THRESHOLD),
        "windy_days": sum(1 for d in data if d["wind_speed"] > WIND_THRESHOLD),
        "rainy_days": sum(1 for d in data if d["precipitation"] > 0),
    }


def export_to_csv(data, file):
    """
    Export the summarized weather data to a CSV file or file-like object.

    Args:
        data (list of dict): The daily weather data to export.
        file (str or file-like object): The name of the CSV file to save the data in, or a file-like object.
    """
    fieldnames = [
        "Date", "Max Temperature", "Min Temperature", "Precipitation",
        "Wind Speed", "Humidity", "Weather Description",
        "Is Hot Day", "Is Windy Day", "Is Rainy Day",
    ]

    def write(handle):
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for d in data:
            writer.writerow({
                "Date": d["date"],
                "Max Temperature": d["max_temperature"],
                "Min Temperature": d["min_temperature"],
                "Precipitation": d["precipitation"],
                "Wind Speed": d["wind_speed"],
                "Humidity": d["humidity"],
                "Weather Description": d.get("weather_description", ""),
                "Is Hot Day": d["max_temperature"] > HOT_THRESHOLD,
                "Is Windy Day": d["wind_speed"] > WIND_THRESHOLD,
                "Is Rainy Day": d["precipitation"] > 0,
            })

    if isinstance(file, str):
        with open(file, "w", newline="", encoding="utf-8") as handle:
            write(handle)
    else:
        write(file)  # file-like object such as StringIO


if __name__ == "__main__":
    # Load the JSON data
    weather_data = load_json("tokyo_weather_complex.json")

    # Summarize the weather data
    summary = summarize_weather_data(weather_data['daily'])

    # Print the summary for verification
    print("Weather Data Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Export the summarized data to a CSV file
    export_to_csv(weather_data['daily'], "tokyo_weather_summary.csv")

    print("Data successfully exported to tokyo_weather_summary.csv")
