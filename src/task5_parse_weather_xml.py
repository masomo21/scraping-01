import xml.etree.ElementTree as ET
import csv


def parse_weather_xml(xml_file):
    """
    Parse weather data from an XML file.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        list of dict: A list of dictionaries with parsed weather data.
    """
    with open(xml_file, "r", encoding="utf-8") as file:
        root = ET.fromstring(file.read())

    data = []
    for day in root.findall("day"):
        data.append({
            "date": day.findtext("date"),
            "temperature": float(day.findtext("temperature")),
            "humidity": int(day.findtext("humidity")),
            "precipitation": float(day.findtext("precipitation")),
        })
    return data


def save_to_csv(data, filename="parsed_weather_data.csv"):
    """
    Save parsed weather data to a CSV file.

    Args:
        data (list of dict): Parsed weather data.
        filename (str): Name of the CSV file.
    """
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Temperature", "Humidity", "Precipitation"])
        for row in data:
            writer.writerow([row["date"], row["temperature"], row["humidity"], row["precipitation"]])


if __name__ == "__main__":
    # Parse the XML file
    weather_data = parse_weather_xml("weather_data.xml")

    # Save the parsed data to a CSV file
    save_to_csv(weather_data)
    print(
        "Data has been successfully parsed and saved to parsed_weather_data.csv."
    )
