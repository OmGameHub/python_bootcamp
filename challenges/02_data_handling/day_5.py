"""
Sample data:
Date,City,Temperature,Condition
2025-06-11,Delhi,36.5,Clear
2025-06-12,Delhi,37.8,Sunny
2025-06-13,Delhi,38.0,Sunny
2025-06-14,Delhi,34.2,Rain
2025-06-15,Delhi,35.0,Clouds
2025-06-16,Delhi,33.4,Rain
2025-06-17,Delhi,34.7,Clear

Plot graphs from this data
"""

import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILE_NAME = "weather_logs.csv"

def visualize_weather():
    dates = []
    temps = []
    weather_conditions = defaultdict(int)

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                dates.append(row["Date"])
                temps.append(float(row["Temperature"]))
                weather_conditions[row["Weather Condition"]] += 1
            except:
                print(f"Error processing row: {row}")
                continue
    
    if not dates:
        print("No valid data found to plot.")
        return
    
    # print(f"Dates: {dates}")
    # print(f"Temperatures: {temps}")
    # print(f"Weather Conditions: {weather_conditions}")
    
    plt.figure(figsize=(10, 7))
    plt.plot(dates, temps, marker="o")
    plt.title("Temperature Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(7, 5))
    plt.bar(weather_conditions.keys(), weather_conditions.values(), color="skyblue")
    plt.xlabel("Weather Condition")
    plt.ylabel("Days Count")
    plt.show()

if __name__ == "__main__":
    visualize_weather()