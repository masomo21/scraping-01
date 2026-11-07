import csv
import re


def clean_text(line):
    """
    Clean the text line by removing non-ASCII characters and fixing known issues.

    Args:
        line (str): The line of text to clean.

    Returns:
        str: The cleaned line of text.
    """
    # Replace non-breaking spaces and other non-ASCII characters
    line = line.replace("\u00a0", " ")          # non-breaking space
    line = line.replace("Â", "")                 # typical encoding artefact
    line = line.replace("°", "")                 # degree sign: "32.9°C" -> "32.9C"
    line = line.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", line).strip()


def extract_weather_data(text_file):
    """
    Extract weather data from a text file using regular expressions.

    Args:
        text_file (str): Path to the text file.

    Returns:
        list of dict: A list of dictionaries with extracted weather data.
    """
    pattern = re.compile(
        r"Date:\s*(\d{4}-\d{2}-\d{2}),\s*"
        r"Max Temp:\s*(-?\d+(?:\.\d+)?)\s*C,\s*"
        r"Min Temp:\s*(-?\d+(?:\.\d+)?)\s*C,\s*"
        r"Humidity:\s*(\d+)\s*%,\s*"
        r"Precipitation:\s*(\d+(?:\.\d+)?)\s*mm"
    )

    extracted_data = []
    with open(text_file, "r", encoding="utf-8") as file:
        for line in file:
            match = pattern.search(clean_text(line))
            if match:
                extracted_data.append({
                    "date": match.group(1),
                    "max_temperature": float(match.group(2)),
                    "min_temperature": float(match.group(3)),
                    "humidity": int(match.group(4)),
                    "precipitation": float(match.group(5)),
                })
    return extracted_data

def save_to_csv(data, filename="extracted_weather_data.csv"):
    """
    Save extracted weather data to a CSV file.

    Args:
        data (list of dict): Extracted weather data.
        filename (str): Name of the CSV file.
    """
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Max Temperature", "Min Temperature", "Humidity", "Precipitation"])
        for row in data:
            writer.writerow([
                row["date"], row["max_temperature"], row["min_temperature"],
                row["humidity"], row["precipitation"],
            ])


if __name__ == "__main__":
    # Extract data from the text file
    weather_data = extract_weather_data("weather_report.txt")

    # Save the extracted data to a CSV file
    save_to_csv(weather_data)
    print(
        "Data has been successfully extracted and saved to extracted_weather_data.csv."
    )
