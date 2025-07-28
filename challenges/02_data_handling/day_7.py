"""
 Challenge: CSV-TO-JSON Converter Tool

"""

import csv
import json
import os

INPUT_FILE = "raw_data.csv"
OUTPUT_FILE = "converted_data.json"

def load_csv_data(file_name):
    if not os.path.exists(file_name):
        print(f"Error: The file {file_name} does not exist.")
        return []
    
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def convert_to_json(data, output_file):
    if not data:
        print("No data to convert.")
        return
    
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    
    print(f"Converted {len(data)} records to {output_file}.")

def main():
    data = load_csv_data(INPUT_FILE)
    if data:
        convert_to_json(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
