import json
import os
import urllib.request

API_KEY = os.environ["EIA_API_KEY"]

BASE_URL = "https://api.eia.gov/v2/electricity/rto/"


def get_json(url):
    separator = "&" if "?" in url else "?"
    url = f"{url}{separator}api_key={API_KEY}"

    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())


def main():
    data = get_json(BASE_URL)

    response = data["response"]

    print("DATASET:")
    print(response.get("name"))
    print()

    print("DESCRIPTION:")
    print(response.get("description"))
    print()

    print("AVAILABLE ROUTES:")
    print("-" * 70)

    for route in response.get("routes", []):
        print(f"ID: {route.get('id')}")
        print(f"Name: {route.get('name')}")
        print(f"Description: {route.get('description')}")
        print("-" * 70)


if __name__ == "__main__":
    main()
