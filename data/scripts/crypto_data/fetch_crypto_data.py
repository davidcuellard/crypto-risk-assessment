import requests
import pandas as pd
import time

def fetch_crypto_data(coin_id='bitcoin', vs_currency='usd', days='30'):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency={vs_currency}&days={days}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
        volumes = pd.DataFrame(data['total_volumes'], columns=['timestamp', 'volume'])
        
        # Convert timestamps
        prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
        volumes['timestamp'] = pd.to_datetime(volumes['timestamp'], unit='ms')
        
        # Merge prices and volumes
        market_data = pd.merge(prices, volumes, on='timestamp')
        print("Data fetched correctly")
        return market_data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

if __name__ == "__main__":
    df = fetch_crypto_data('bitcoin', 'usd', '30')
    if df is not None:
        df.to_csv('../../raw/bitcoin_30days.csv', index=False)
        print(df.head())

