"""
 Challenge: Quote of the Day Image Maker

Goal:
- Scrape random quotes from https://quotes.toscrape.com/
- Extract quote text and author for the first 5 quotes
- Create an image for each quote using PIL
- Save images in 'quotes/' directory using filenames like quote_1.png, quote_2.png, etc.
"""

import os
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont


BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "images/quotes"

def fetch_quotes():
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching quotes: {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    extracted_quotes = []
    for quote in quotes[:5]:
        text = quote.find("span", class_="text").text.strip("“”")
        author = quote.find("small", class_="author").text.strip()

        extracted_quotes.append((text, author))
    
    return extracted_quotes

def create_image(text, author, idx):
    width, height = 800, 400
    bg_color = "#f8d77f"
    text_color = "#262626"

    image = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()
    author_font = ImageFont.load_default()

    wrapped_text = textwrap.fill(text, width=60)
    author_text = f"- {author}"

    y_text = 60
    draw.text((40, y_text), wrapped_text, font=font, fill=text_color)
    y_text += wrapped_text.count("\n") * 15 + 40
    draw.text((500, y_text), author_text, font=font, fill=text_color)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = os.path.join(OUTPUT_DIR, f"quote_{idx + 1}.png")
    image.save(filename)
    print(f"Saved image: {filename}")

def main():
    quotes = fetch_quotes()
    if not quotes:
        print("No quotes found.")
        return

    for idx, (text, author) in enumerate(quotes):
        create_image(text, author, idx)

if __name__ == "__main__":
    main()