# JSON File Reader

import json

filename = "data.json"

try:
    with open(filename, 'r') as file:
        data = json.load(file)

        print(f"Data from {filename}:")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")

except FileNotFoundError:
    print(f"Error: {filename} not found.")
except json.JSONDecodeError:
    print("Error: Could not decode JSON.")
