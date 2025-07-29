"""
 Challenge: Download Cover Images of First 10 Books

Goal:
- Visit https://books.toscrape.com/
- Scrape the first 10 books listed on the homepage
- For each book, extract:
  • Title
  • Image URL

Then:
- Download each image
- Save it to a local `images/` folder with the filename as the book title (sanitized)

Example:
 Title: "A Light in the Attic"
 Saved as: images/A_Light_in_the_Attic.jpg

Bonus:
- Handle invalid filename characters
- Show download progress
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re

BASE_URL = "https://books.toscrape.com"
IMAGE_DIR = "images"
TARGET_BOOKS_COUNT = 10

def sanitize_filename(title: str) -> str:
    return re.sub(r"[^\w\-.]", "", title).replace(" ", "_")

def download_image(image_url: str, filename: str):
    try:
        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status()

        with open(filename, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
        return

def scrape_and_download_books_images(page_url):
    try:
        response = requests.get(page_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page:\n{e}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:TARGET_BOOKS_COUNT]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    
    for book in books:
        title = book.h3.a["title"]
        image_url = urljoin(BASE_URL, book.find("img")["src"])

        filename = f"{sanitize_filename(title)}.jpg"
        filepath = os.path.join(IMAGE_DIR, filename)

        print(f"Downloading: {filepath}")
        download_image(image_url, filepath)

    print(f"Downloaded images for {len(books)} books.")
    
def main():
    print(f"Starting to scrape and download images for the first {TARGET_BOOKS_COUNT} books...")
    scrape_and_download_books_images(BASE_URL)
    print("Done.")


if __name__ == "__main__":
    main()