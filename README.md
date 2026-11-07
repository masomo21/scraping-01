# Data Collection and Scraping

## Setup

Before performing the task, you need to set up the development environment.

### Creating a Python virtual environment

1. For Windows:
    ```powershell
    python -m venv venv
    ```

2. For Linux/macOS:
    ```bash
    python3 -m venv venv
    ```

### Activating the virtual environment

1. For Windows:
    ```powershell
    .\venv\Scripts\activate
    ```

2. For Linux/macOS:
    ```bash
    source venv/bin/activate
    ```

> [!NOTE]
> After activating the virtual environment, you will see the `(venv)` prefix in front of the command line.

### Installing the required packages from the `requirements.txt` file

1. For both systems:
    ```bash
    pip install -r requirements.txt
    ```


## Task 1. Basic Web Scraping and JSON Storage

Create a Python script that performs basic web scraping on a Wikipedia page to extract specific information and then saves this information in a JSON file.

**Tasks:**

1. **Fetch a Wikipedia Page:**
   - Write a Python function that retrieves the HTML content of the Wikipedia page for "Web scraping" using the `requests` library.

2. **Extract the Page Title:**
   - Write a Python function that parses the HTML content using `BeautifulSoup` and extracts the title of the page (`<h1>` element with `id="firstHeading"`).

3. **Extract the First Sentence of the First Paragraph:**
   - Write a Python function that extracts the first sentence from the first paragraph (`<p>` element) on the page.

4. **Store the Extracted Information in a JSON File:**
   - Write a Python function that saves the extracted title and first sentence into a JSON file.

**Expected JSON Output:**

The JSON file should contain the following structure:

```json
{
    "title": "Web scraping",
    "first_sentence": "Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites."
}
```

**Implementation Details:**

- **Libraries Used:** `requests`, `BeautifulSoup`, `json`, `pytest`
- **Testing:** Use `pytest` to implement unit tests for each function.
- **File Handling:** The extracted data should be saved to a JSON file named `extracted_wikipedia_data.json`.



## Task 2: Collecting Weather Data Using Open-Meteo API

Learn how to collect weather data using the Open-Meteo API and save the extracted data into a JSON file.

### Task Description:

1. **Fetch Weather Data:**
   - Write a Python script that sends a request to the Open-Meteo API using the provided endpoint:
     - URL: `https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&daily=temperature_2m_max&timezone=Asia/Tokyo`
   - This URL fetches the maximum temperature forecast for Tokyo (latitude 35.6895, longitude 139.6917).

2. **Extract the Maximum Temperature:**
   - Extract the `temperature_2m_max` value from the JSON response. This represents the maximum temperature for the next day in Tokyo.

3. **Save the Extracted Data:**
   - Save the extracted temperature data into a JSON file named `tokyo_weather.json`.

### JSON Output Example:

The JSON file might look like this:

```json
{
    "date": "2024-08-18",
    "max_temperature": 32.5
}
```

## Task 3: Advanced Parsing, Analyzing, and Reporting on Complex Weather Data

Create a Python script that loads, parses, and analyzes complex weather data stored in a JSON file. The script should perform multiple analyses over several days and generate detailed reports summarizing the findings.

### Task Description:

1. **Load the JSON Data:**
   - Write a Python script that loads weather data from a JSON file named `tokyo_weather_complex.json`.

2. **Parse the JSON Data:**
   - Extract relevant information from the JSON data, including:
     - City name, geographical coordinates (latitude, longitude), and timezone.
     - Daily weather data, including the date, maximum and minimum temperatures, precipitation, wind speed, humidity, and a short weather description.

3. **Perform Multiple Analyses:**
   - **Temperature Analysis:** For each day, check if the maximum temperature exceeds a specified threshold (e.g., 30°C) and determine if it’s a hot day.
   - **Temperature Swing Analysis:** Calculate the difference between the maximum and minimum temperatures for each day. Determine if there was a significant temperature swing (e.g., more than 10°C).
   - **Wind Analysis:** Check if the wind speed exceeded a specified threshold (e.g., 15 km/h) and determine if it was a windy day.
   - **Humidity and Comfort Analysis:** Assess the humidity level and determine if the day was likely to be uncomfortable (e.g., if humidity is over 70%).
   - **Precipitation Analysis:** Identify rainy days and determine the severity of the rain (e.g., light, moderate, or heavy rain based on precipitation levels).

4. **Generate Detailed Reports:**
   - For each day, generate a detailed report that summarizes the findings from the analyses. The report should include:
     - The date and weather description.
     - An assessment of whether it was a hot day, the significance of the temperature swing, whether it was windy, and whether the humidity made the day uncomfortable.
     - Information on whether it was a rainy day or if there was no precipitation.
   - Provide a summary report that highlights:
     - The hottest day.
     - The windiest day.
     - The most humid day.
     - The day with the most precipitation.

**The output**
```
Date: 2024-08-18
Weather: Clear sky
Temperature: Max 10.0°C
It was a hot day.
It was a windy day.
There was no precipitation.

Date: 2024-08-19
Weather: Light rain
Temperature: Max 9.0°C
It was a rainy day.

Date: 2024-08-20
Weather: Moderate rain
Temperature: Max 8.0°C
The humidity made the day uncomfortable.
It was a rainy day.

Date: 2024-08-21
Weather: Sunny
Temperature: Max 9.0°C
It was a hot day.
It was a windy day.
There was no precipitation.

Weather Summary:
Hottest day: 2024-08-18 with a maximum temperature of 10.0°C
Windiest day: 2024-08-18 with wind speeds of True km/h
Most humid day: 2024-08-20 with a humidity level of True%
Rainiest day: 2024-08-19 with True mm of precipitation
```

## Task 4: Summarizing and Exporting Weather Data to CSV

Create a Python script that loads, summarizes, and exports complex weather data stored in a JSON file to a CSV file. The script should be able to handle both file paths and file-like objects for the CSV output.

### Task Description:

1. **Load and Parse JSON Data:**
   - Write a Python script that loads weather data from a JSON file named `tokyo_weather_complex.json`.

2. **Summarize Weather Data:**
   - Implement a function that calculates key metrics across multiple days of weather data. The summary should include:
     - The average maximum and minimum temperatures over the period.
     - The total precipitation over the period.
     - The average wind speed and humidity over the period.
     - The number of hot days (e.g., days where the temperature exceeded 30°C).
     - The number of windy days (e.g., days where the wind speed exceeded 15 km/h).
     - The number of rainy days.

3. **Export the Summary to a CSV File:**
   - Create a function that exports the summarized data to a CSV file. The function should:
     - Accept either a string (file path) or a file-like object (e.g., `StringIO`) as the destination for the CSV output.
     - Write the daily weather data, including additional analyzed metrics (e.g., whether it was a hot day, windy day, or rainy day).
     - Ensure the CSV file includes appropriate headers.

### Example Implementation:

Here’s a breakdown of the key functions:

1. **load_json:**
   - Loads the JSON data from the specified file.

2. **summarize_weather_data:**
   - Summarizes key metrics across all days, such as average temperatures, total precipitation, average wind speed, and counts of hot, windy, and rainy days.

3. **export_to_csv:**
   - Exports the summarized weather data to a CSV file. This function should handle both string filenames and file-like objects.

### Example CSV Output:

The CSV file might look like this:

```csv
Date,Max Temperature,Min Temperature,Precipitation,Wind Speed,Humidity,Weather Description,Is Hot Day,Is Windy Day,Is Rainy Day
2024-08-18,32.5,22.5,0.0,15.5,65,Clear sky,True,True,False
2024-08-19,30.0,21.0,5.0,10.0,70,Light rain,False,False,True
2024-08-20,28.0,20.0,10.0,8.0,80,Moderate rain,False,False,True
2024-08-21,33.0,24.0,0.0,20.0,60,Sunny,True,True,False
```

## Task 5: Parsing Weather Data from an XML File

Create a Python script to parse weather data from an XML file, extract key metrics, and store them in a CSV file.

**Task Description:**

1. **Load XML Data:**
   - You are provided with an XML file named `weather_data.xml` containing weather information for several days. The XML structure includes elements like `<date>`, `<temperature>`, `<humidity>`, and `<precipitation>`.

2. **Parse the XML File:**
   - Write a Python script to load and parse the XML file using the `xml.etree.ElementTree` module.
   - Extract the date, temperature, humidity, and precipitation for each day from the XML structure.

3. **Store Data in CSV:**
   - Store the extracted data in a CSV file named `parsed_weather_data.csv` with the following headers:
     - `Date`
     - `Temperature`
     - `Humidity`
     - `Precipitation`

**Example XML Structure:**

```xml
<weather>
    <day>
        <date>2024-08-18</date>
        <temperature>32.9</temperature>
        <humidity>65</humidity>
        <precipitation>0.0</precipitation>
    </day>
    <day>
        <date>2024-08-19</date>
        <temperature>30.5</temperature>
        <humidity>70</humidity>
        <precipitation>1.2</precipitation>
    </day>
    <!-- More day elements -->
</weather>
```

**Expected Output:**
- A CSV file named `parsed_weather_data.csv` with rows of weather data extracted from the XML file.


## Task 6: Extracting Data Using Regular Expressions

Create a Python script to extract weather data from a text file using regular expressions and store the data in a CSV file.

**Task Description:**

1. **Text Data Extraction:**
   - You are provided with a text file named `weather_report.txt` containing daily weather summaries in the following format:
     ```
     Date: 2024-08-18, Max Temp: 32.9°C, Min Temp: 22.5°C, Humidity: 65%, Precipitation: 0.0mm
     Date: 2024-08-19, Max Temp: 30.5°C, Min Temp: 21.8°C, Humidity: 70%, Precipitation: 1.2mm
     ```
   
2. **Extract Data Using Regular Expressions:**
   - Write a Python script to extract the date, maximum temperature, minimum temperature, humidity, and precipitation from each line using regular expressions.
   - Ensure that the script can handle any issues related to text encoding, such as non-ASCII characters, by cleaning the data before extraction.

3. **Store Extracted Data in CSV:**
   - Store the extracted data in a CSV file named `extracted_weather_data.csv` with the following headers:
     - `Date`
     - `Max Temperature`
     - `Min Temperature`
     - `Humidity`
     - `Precipitation`

**Expected Output:**
- A CSV file named `extracted_weather_data.csv` with rows of weather data extracted from the text file.









