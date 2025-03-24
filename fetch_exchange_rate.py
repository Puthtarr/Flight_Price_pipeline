import requests
import pandas as pd
from datetime import datetime, timedelta
from settings import *

def fetch_exchange_rates_apilayer(date, base_currency="THB"):
    print(f'Date for get Data : {date}')
    url = f"https://api.apilayer.com/exchangerates_data/{date}"
    params = {
        "base": base_currency
    }

    headers = {
        "apikey": EXCHANGE_RATE_ACCESS_KEY
    }

    print(f"Requesting: {url} with params: {params}")
    response = requests.get(url, headers=headers, params=params)

    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Response JSON: {data}")

    if response.status_code == 200 and 'rates' in data:
        rates = data['rates']
        df_rates = pd.DataFrame(list(rates.items()), columns=['currency', f'rate_to_{base_currency}'])
        print(f"Rates for {date}")
        print(df_rates.head(5))

    else:
        print(f"Failed to fetch rates for {date}")
        return None

    filename = f'exchange_rate_{date}.csv'
    df_rates.to_csv(RAW_EXCHANGE_RATE_DIR + os.sep + filename)
    return df_rates

if __name__ == '__main__':
    date_x = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    fetch_exchange_rates_apilayer(date=date_x)


