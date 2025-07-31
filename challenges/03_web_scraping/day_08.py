"""
depends on:
 - Day 7 of web scraping

Fetch crypto data every hour automatically
"""

import requests
import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import schedule
import time

BASE_API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False,
}

CSV_FILE = "crypto_prices.csv"

def fetch_crypto_prices():
    try:
        response = requests.get(BASE_API_URL, params=PARAMS)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    
    return response.json()

def save_to_file(data):
    is_file = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not is_file:
            writer.writerow(["timestamp", "coin", "price"])

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin["current_price"]])

    print(f"Data saved to {CSV_FILE}")

def fetch_and_save_crypto_data_job():
    print("Fetching crypto prices...")
    crypto_data = fetch_crypto_prices()
    
    if not crypto_data:
        print("No data fetched.")
        return
    
    save_to_file(crypto_data)
    print("Data fetching and saving complete.")

if __name__ == "__main__":
    schedule.every().hour.do(fetch_and_save_crypto_data_job)

    while True:
        schedule.run_pending()
        time.sleep(60)