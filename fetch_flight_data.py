import requests
import pandas as pd
from datetime import datetime
from pathlib import Path
from settings import *

RAW_FLIGHT_DATA_DIR = Path('data/raw/flights')
RAW_FLIGHT_DATA_DIR.mkdir(parents=True, exist_ok=True)

def fetch_live_flight_data(limit=50):
    url = 'http://api.aviationstack.com/v1/flights'

    params = {
        'access_key': AVIATIONSTACK_ACCESS_KEY,
        'limit': limit
    }

    print(f"Requesting Live Flight Data from: {url}")
    print(f"Params: {params}")

    response = requests.get(url, params=params)
    print(f"Status Code: {response.status_code}")

    try:
        data = response.json()
        print(f"Response JSON Preview: {data if len(str(data)) < 1000 else 'Too long to display'}")

        if response.status_code == 200 and 'data' in data:
            flights = data['data']
            if flights:
                df = pd.json_normalize(flights)
                print(f"Retrieved {len(df)} live flight records.")

                # Save to CSV with today's date
                date_str = datetime.now().strftime('%Y-%m-%d')
                filename = f'flights_live_{date_str}.csv'
                file_path = RAW_FLIGHT_DATA_DIR / filename
                df.to_csv(file_path, index=False)
                print(f"Saved file: {file_path}")

                return df
            else:
                print("No live flight data found.")
                return None
        else:
            print(f"Failed. Error Message: {data.get('error', 'No error info')}")
            return None

    except Exception as e:
        print(f"Exception occurred: {e}")
        return None


if __name__ == '__main__':
    fetch_live_flight_data(limit=100)
