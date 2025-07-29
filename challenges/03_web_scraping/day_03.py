"""
 Challenge: Scrape Books To Scrape (70 Books)

Goal:
- Visit https://books.toscrape.com/
- Scrape each book's:
  • Title 
  • Price 

You must:
- Crawl through multiple pages using the "next" button until you collect 70 books.
- Save the data to a JSON file: books_data.json
- Handle network errors gracefully.

Bonus:
- Track how many books scraped
- Print progress as you collect pages
"""

import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com"
START_PAGE = "catalogue/page-1.html"
OUTPUT_FILE = "books_data.json"
TARGET_BOOKS_COUNT = 70

def scrape_page(page_url):
    try:
        response = requests.get(page_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page:\n{e}")
        return [], None
    
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")
        price = article.select_one("p.price_color").text.strip()

        books.append({ "title": title, "price": price })
    
    next_link = soup.select_one("li.next > a")
    next_url = urljoin(page_url, next_link.get("href")) if next_link else None

    return books, next_url

def save_books_to_json(books):
    if not books:
        print("No books to save.")
        return
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=2)

    print(f"Saved {len(books)} books to {OUTPUT_FILE}")

def main():
    collected_books = []
    current_page_url = urljoin(BASE_URL, START_PAGE)
    
    while len(collected_books) < TARGET_BOOKS_COUNT and current_page_url:
        print(f"Scraping page: {current_page_url}")
        books, next_page_url = scrape_page(current_page_url)
        collected_books.extend(books)
        current_page_url = next_page_url

    collected_books = collected_books[:TARGET_BOOKS_COUNT]
    if not collected_books:
        print("No books were collected.")
        return
    
    print(f"Total books collected: {len(collected_books)}")
    save_books_to_json(collected_books)

if __name__ == "__main__":
    main()