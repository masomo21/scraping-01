import json


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


def analyze_daily_weather(day, temp_threshold=30, wind_threshold=15, humidity_threshold=70):
    """
    Analyze weather data for a single day.

    Args:
        day (dict): The weather data for the day.
        temp_threshold (float): The temperature threshold to determine a hot day.
        wind_threshold (float): The wind speed threshold to determine a windy day.
        humidity_threshold (float): The humidity threshold to determine uncomfortable weather.

    Returns:
        dict: A dictionary with analysis results for the day.
    """
    precipitation = day.get("precipitation", 0.0)
    return {
        "date": day["date"],
        "weather_description": day.get("weather_description", ""),
        "max_temperature": day["max_temperature"],
        "min_temperature": day["min_temperature"],
        "wind_speed": day.get("wind_speed", 0.0),
        "humidity": day.get("humidity", 0),
        "precipitation": precipitation,
        "is_hot_day": day["max_temperature"] > temp_threshold,
        "temperature_swing": round(day["max_temperature"] - day["min_temperature"], 1),
        "is_large_swing": (day["max_temperature"] - day["min_temperature"]) > 10,
        "is_windy_day": day.get("wind_speed", 0.0) > wind_threshold,
        "is_uncomfortable_day": day.get("humidity", 0) > humidity_threshold,
        "is_rainy_day": precipitation > 0,
        "rain_severity": classify_rain(precipitation),
    }


def classify_rain(precipitation):
    """
    Classify rainfall severity by the amount of precipitation (mm).

    Returns:
        str: "none", "light", "moderate" or "heavy".
    """
    if precipitation <= 0:
        return "none"
    if precipitation <= 5:
        return "light"
    if precipitation <= 10:
        return "moderate"
    return "heavy"


def generate_daily_report(analysis):
    """
    Generate a detailed report based on the analysis results for a single day.

    Args:
        analysis (dict): The analysis results for the day.

    Returns:
        str: A detailed report as a string.
    """
    lines = [f"Weather report for {analysis['date']}: {analysis.get('weather_description', '')}"]
    lines.append(f"Temperature: Max {analysis['temperature_swing']}°C swing between day and night")
    lines.append("- It is a hot day." if analysis.get("is_hot_day") else "- It is not a hot day.")
    lines.append("- It is a windy day." if analysis.get("is_windy_day") else "- It is not a windy day.")
    if analysis.get("is_uncomfortable_day"):
        lines.append("- Humidity is uncomfortable.")
    else:
        lines.append("- Humidity is comfortable.")
    if analysis.get("is_rainy_day"):
        severity = analysis.get("rain_severity", "some")
        lines.append(f"- Rain expected ({severity}).")
    else:
        lines.append("- There is no precipitation.")
    return "\n".join(lines)



def summarize_weather_analysis(analyses):
    """
    Summarize the weather analysis over multiple days.

    Args:
        analyses (list of dict): A list of daily analysis results.

    Returns:
        str: A summary report as a string.
    """
    if not analyses:
        return "No data to summarize."

    def day_with_max(key, fallback):
        best = max(analyses, key=lambda a: a.get(key, a.get(fallback, 0)))
        return best["date"]

    hottest = day_with_max("max_temperature", "is_hot_day")
    windiest = day_with_max("wind_speed", "is_windy_day")
    most_humid = day_with_max("humidity", "is_uncomfortable_day")
    rainiest = day_with_max("precipitation", "is_rainy_day")

    hot_count = sum(1 for a in analyses if a.get("is_hot_day"))
    windy_count = sum(1 for a in analyses if a.get("is_windy_day"))
    rainy_count = sum(1 for a in analyses if a.get("is_rainy_day"))

    return "\n".join([
        f"Summary for {len(analyses)} days:",
        f"Hottest day: {hottest}",
        f"Windiest day: {windiest}",
        f"Most humid day: {most_humid}",
        f"Rainiest day: {rainiest}",
        f"Hot days: {hot_count}, windy days: {windy_count}, rainy days: {rainy_count}",
    ])


if __name__ == "__main__":
    # Load the JSON data
    weather_data = load_json("tokyo_weather_complex.json")

    # Analyze the weather data for each day
    analyses = [analyze_daily_weather(day) for day in weather_data['daily']]

    # Generate and print daily reports
    for analysis in analyses:
        report = generate_daily_report(analysis)
        print(report)

    # Generate and print a summary report
    summary_report = summarize_weather_analysis(analyses)
    print(summary_report)
