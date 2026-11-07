import requests
from bs4 import BeautifulSoup
import json
import re


def fetch_wikipedia_page(url):
    """
    Fetch the HTML content of the given Wikipedia page.

    Args:
        url (str): The URL of the Wikipedia page to fetch.

    Returns:
        str: The HTML content of the page as a string.

    Raises:
        HTTPError: If the HTTP request returned an unsuccessful status code.
    """
    headers = {"User-Agent": "Mozilla/5.0 (educational scraping exercise)"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text


def extract_title(soup):
    """
    Extract the title of the Wikipedia page.

    Args:
        soup (BeautifulSoup): A BeautifulSoup object representing the parsed HTML.

    Returns:
        str: The title of the page.
    """
    heading = soup.find(id="firstHeading")
    if heading is not None:
        return heading.get_text(strip=True)
    if soup.title is not None and soup.title.string:
        return soup.title.string.replace(" - Wikipedia", "").strip()
    return None


def extract_first_sentence(soup):
    """
    Extract the first sentence of the first paragraph on the Wikipedia page.

    Args:
        soup (BeautifulSoup): A BeautifulSoup object representing the parsed HTML.

    Returns:
        str: The first sentence of the first paragraph.
    """
    for paragraph in soup.find_all("p"):
        text = paragraph.get_text(" ", strip=True)
        text = re.sub(r"\[\s*\d+\s*\]", "", text)   # remove references like [1]
        text = re.sub(r"\s+", " ", text).strip()
        text = re.sub(r"\s+([.,;:)])", r"\1", text)
        if not text:
            continue  # skip empty paragraphs
        match = re.match(r"(.+?[.!?])(?=\s|$)", text)
        return match.group(1) if match else text
    return None


def save_to_json(data, filename):
    """
    Save the extracted data to a JSON file.

    Args:
        data (dict): The data to be saved to the JSON file.
        filename (str): The name of the JSON file to save the data in.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    page_content = fetch_wikipedia_page(url)
    soup = BeautifulSoup(page_content, 'html.parser')

    # Extract the title of the page
    title = extract_title(soup)

    # Extract the first sentence of the first paragraph
    first_sentence = extract_first_sentence(soup)

    # Combine the extracted data
    extracted_data = {"title": title, "first_sentence": first_sentence}

    # Print the extracted data
    print("Extracted Data:", extracted_data)

    # Save the data to a JSON file
    save_to_json(extracted_data, 'extracted_wikipedia_data.json')

    print("Data successfully saved to extracted_wikipedia_data.json")
