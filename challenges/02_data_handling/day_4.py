"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import os
import csv
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

FILE_NAME = "weather_logs.csv"
API_KEY = os.getenv("WEATHER_API_KEY")

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "City", "Temperature (°C)", "Weather Condition"])
        
def fetch_weather_by_city_name(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
     
    if response.status_code != 200:
        print(f"API Error: {response.get("message", "Unknown error")}")
        return None
    else:
        return response.json()

def log_weather_data():
    date = datetime.now().strftime("%Y-%m-%d")
    city_name = input("Enter the city name: ")
    
    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"] == date and row["City"].lower() == city_name.lower():
                print("Weather data for this city on today's date already exists.")
                return
    
    try:
        weather_data = fetch_weather_by_city_name(city_name)
        if not weather_data:
            return
        
        temperature = weather_data["main"]["temp"]
        weather_condition = weather_data["weather"][0]["main"]

        with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([date, city_name, temperature, weather_condition])
            print("Weather data logged successfully.")
    except Exception as e:
        print(f"Failed to log weather data: {e}")

def view_all_weather_logs():
    try:
        with open(FILE_NAME, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            logs = list(reader)
            if not logs:
                print("No weather logs found.")
                return
            
            print("\nWeather Logs:")
            print(f"{'Date':<15} {'City':<20} {'Temperature (°C)':<20} {'Weather Condition':<20}")
            for log in logs:
                print(f"{log['Date']:<15} {log['City']:<20} {log['Temperature (°C)']:<20} {log['Weather Condition']:<20}")
    except FileNotFoundError:
        print("No weather logs found. Please log some data first.")

def show_statistics():
    try:
        with open(FILE_NAME, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            logs = list(reader)
            if not logs:
                print("No weather logs found.")
                return
            
            temperatures = [float(log["Temperature (°C)"]) for log in logs]
            conditions = [log["Weather Condition"] for log in logs]

            avg_temp = sum(temperatures) / len(temperatures)
            max_temp = max(temperatures)
            min_temp = min(temperatures)
            most_frequent_condition = max(set(conditions), key=conditions.count)

            print(f"\nStatistics:")
            print(f"Average Temperature: {avg_temp:.2f} °C")
            print(f"Highest Temperature: {max_temp:.2f} °C")
            print(f"Lowest Temperature: {min_temp:.2f} °C")
            print(f"Most Frequent Weather Condition: {most_frequent_condition}")
    except FileNotFoundError:
        print("No weather logs found. Please log some data first.")

def main():
    while True:
        print("\nWeather Logger Menu:")
        print("1. Add new weather log")
        print("2. View all logs")
        print("3. Show statistics")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        match choice:
            case "1": log_weather_data()
            case "2": view_all_weather_logs()
            case "3": show_statistics()
            case "4":
                print("Exiting the program. Goodbye!")
                break
            case _: print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if not API_KEY:
        print("Please set the WEATHER_API_KEY in the .env file.")
    else:
        main()