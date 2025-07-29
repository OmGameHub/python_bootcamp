"""
 Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.
"""

import csv
import requests
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com"
CSV_FILE = "hn_top20.csv"

def fetch_hn_top_posts(limit=20):
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page:\n${e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("span.titleline > a")

    posts = []
    for link in post_links[: limit]:
        title = link.get_text(strip=True)
        url = link.get("href")
        posts.append({ "Title": title, "URL": url })
    return posts

def save_to_csv(posts, filename=CSV_FILE):
    if not posts:
        print("No posts to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "URL"])
        writer.writeheader()
        writer.writerows(posts)
    print(f"Saved {len(posts)} posts to {filename}")


def main():
    print("Scraping Hacker News top posts...")
    top_posts = fetch_hn_top_posts()

    print("Collected all top posts.")
    save_to_csv(top_posts)

if __name__ == "__main__":
    main()
        
