"""
 Challenge: Store & Search Crypto Prices in SQLite

Goal:
- Save hourly top 10 crypto prices into a local SQLite database
- Each record should include timestamp, coin ID, and price
- Allow the user to search for a coin by name and return the latest price

Teaches: SQLite handling in Python, data storage, search queries, API + DB integration
"""

import requests
from datetime import datetime
import sqlite3

BASE_API_URL = "https://api.coingecko.com/api/v3/coins/markets"

DB_NAME = "crypto.db"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False,
}

def fetch_crypto_prices():
    try:
        response = requests.get(BASE_API_URL, params=PARAMS)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    
    return response.json()

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            coin_id TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for coin in data:
        cursor.execute('''
            INSERT INTO crypto_prices (timestamp, coin_id, price)
            VALUES (?, ?, ?)
        ''', (timestamp, coin["id"], coin["current_price"]))
    
    conn.commit()
    conn.close()
    print(f"Data saved to {DB_NAME}")

def search_coin(coin_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT timestamp, price FROM crypto_prices
        WHERE coin_id = ?
        ORDER BY timestamp DESC
        LIMIT 1
    ''', (coin_name, ))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        print(f"Latest price for {coin_name}: {result[1]} at {result[0]}")
    else:
        print(f"No data found for coin: {coin_name}")

def main():
    create_table()

    while True:
        print("-" * 30)
        print("\nMenu:")
        print("1. Fetch and save crypto data")
        print("2. Search for a coin by name")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                print("Fetching crypto prices...")
                crypto_data = fetch_crypto_prices()
                
                if not crypto_data:
                    print("No data fetched.")
                    continue
                
                save_to_db(crypto_data)
                print("Data fetching and saving complete.")
            case "2":
                coin_name = input("Enter the coin ID to search: ").strip().lower()
                search_coin(coin_name)
            case "3":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

