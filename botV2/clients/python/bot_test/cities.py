import json

def load_cities(file_path):
    """Load cities from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['city']

def city_exists(city_name, cities):
    """Check if a city exists in the list of cities."""
    for city in cities:
        if city['name'].lower() == city_name.lower():
            return True
    return False

def main(city_name):
    """Main function to check if a city exists."""
    cities = load_cities('Cities.json')
    return city_exists(city_name, cities)

# Example usage
if __name__ == "__main__":
    city_to_check = "Балларат"  # Replace with the desired city name
    exists = main(city_to_check)
    print(f"Does the city '{city_to_check}' exist? {exists}")