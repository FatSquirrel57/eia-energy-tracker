import json
import os
import urllib.parse
import urllib.request

API_KEY = os.environ["EIA_API_KEY"]

BASE_URL = "https://api.eia.gov/v2/electricity/rto/region-data/data/"


def get_eia_data():
    params = {
        "api_key": API_KEY,
        "frequency": "hourly",
        "data[0]": "value",
        "facets[respondent][]": "US48",
        "facets[type][]": "D",
        "sort[0][column]": "period",
        "sort[0][direction]": "desc",
        "length": 10
    }

    url = BASE_URL + "?" + urllib.parse.urlencode(params)

    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())


def main():
    data = get_eia_data()

    rows = data["response"]["data"]

    print(f"Rows returned: {len(rows)}")
    print()

    for row in rows:
        print(
            row["period"],
            row.get("respondent-name"),
            row.get("type-name"),
            row["value"],
            row.get("value-units")
        )


if __name__ == "__main__":
    main()
