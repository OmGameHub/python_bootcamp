"""
 Challenge: Crypto Price Tracker with Graphs

Goal:
- Fetch live prices of the top 10 cryptocurrencies using CoinGecko's free public API
- Store prices in a CSV file with timestamp
- Generate a line graph for a selected coin over time (price vs. time)
- Repeatable — user can run this multiple times to log data over time

JSON handling, API usage, CSV storage, matplotlib graphing
"""

import requests
import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt

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


def plot_coin_prices(coin_id):
    times = []
    prices = []

    with open(CSV_FILE, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["coin"] == coin_id:
                times.append(row["timestamp"])
                prices.append(float(row["price"]))

    if not times or not prices:
        print(f"No data found for coin: {coin_id}")
        return
    
    plt.figure(figsize=(10, 5))
    plt.plot(times, prices, marker="o")
    plt.tight_layout()
    plt.grid()
    plt.show()

def main():
    print("Fetching crypto prices...")
    crypto_data = fetch_crypto_prices()
    
    if not crypto_data:
        print("No data fetched.")
        return
    
    save_to_file(crypto_data)
    print("Data fetching and saving complete.")
    

    print("-" * 30)
    for coin in crypto_data:
        print(f"{coin['name']} ({coin['id']}): ${coin['current_price']:.2f}")
    print("-" * 30)

    coin_id = input("Enter the coin ID to plot (e.g., bitcoin, ethereum): ").strip().lower()
    plot_coin_prices(coin_id)

if __name__ == "__main__":
    main()