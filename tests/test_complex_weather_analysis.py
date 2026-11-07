import pytest
import json
from src.task3_complex_weather_analysis import load_json, analyze_daily_weather, generate_daily_report, summarize_weather_analysis


def test_load_json(monkeypatch):
    # Mock JSON data
    mock_data = {
        "city": "Tokyo",
        "latitude": 35.6895,
        "longitude": 139.6917,
        "timezone": "Asia/Tokyo",
        "daily": [
            {
                "date": "2024-08-18",
                "max_temperature": 32.5,
                "min_temperature": 22.5,
                "precipitation": 0.0,
                "wind_speed": 15.5,
                "humidity": 65,
                "weather_description": "Clear sky"
            }
        ]
    }

    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO(json.dumps(mock_data))

    monkeypatch.setattr('builtins.open', mock_open)

    # Call the function and check the content
    data = load_json("tokyo_weather_complex.json")
    assert data["city"] == "Tokyo"
    assert len(data["daily"]) == 1


def test_analyze_daily_weather():
    # Mock daily weather data
    day = {
        "date": "2024-08-18",
        "max_temperature": 32.5,
        "min_temperature": 22.5,
        "precipitation": 0.0,
        "wind_speed": 15.5,
        "humidity": 65,
        "weather_description": "Clear sky"
    }

    # Call the function and check the analysis results
    analysis = analyze_daily_weather(day)
    assert analysis["date"] == "2024-08-18"
    assert analysis["is_hot_day"] is True
    assert analysis["temperature_swing"] == 10.0
    assert analysis["is_windy_day"] is True
    assert analysis["is_uncomfortable_day"] is False
    assert analysis["is_rainy_day"] is False


def test_generate_daily_report():
    # Mock analysis data
    analysis = {
        "date": "2024-08-18",
        "is_hot_day": True,
        "temperature_swing": 10.0,
        "is_windy_day": True,
        "is_uncomfortable_day": False,
        "is_rainy_day": False,
        "weather_description": "Clear sky"
    }

    # Call the function and check the report
    report = generate_daily_report(analysis)
    assert "2024-08-18" in report
    assert "Clear sky" in report
    assert "hot day" in report
    assert "windy day" in report
    assert "Temperature: Max 10.0°C" in report
    assert "no precipitation" in report


def test_summarize_weather_analysis():
    # Mock list of analysis data
    analyses = [
        {
            "date": "2024-08-18",
            "is_hot_day": True,
            "temperature_swing": 10.0,
            "is_windy_day": True,
            "is_uncomfortable_day": False,
            "is_rainy_day": False,
            "weather_description": "Clear sky"
        },
        {
            "date": "2024-08-19",
            "is_hot_day": False,
            "temperature_swing": 8.0,
            "is_windy_day": False,
            "is_uncomfortable_day": True,
            "is_rainy_day": True,
            "weather_description": "Light rain"
        }
    ]

    # Call the function and check the summary report
    summary = summarize_weather_analysis(analyses)
    assert "Hottest day" in summary
    assert "Windiest day" in summary
    assert "Most humid day" in summary
    assert "Rainiest day" in summary


if __name__ == "__main__":
    pytest.main()
