import pandas as pd
import numpy as np

# Load market data
market_data = pd.read_csv('../../raw/bitcoin_30days.csv')

# Convert timestamp to datetime
market_data['timestamp'] = pd.to_datetime(market_data['timestamp'])

# Sort data by timestamp
market_data.sort_values('timestamp', inplace=True)
market_data.reset_index(drop=True, inplace=True)

# Calculate daily returns
market_data['price_return'] = market_data['price'].pct_change()

# Feature 1: Volatility (Rolling Standard Deviation of Returns)
market_data['volatility'] = market_data['price_return'].rolling(window=7).std()

# Feature 2: Liquidity (Use Volume)
market_data['liquidity'] = market_data['volume']

# Feature 3: Price Momentum (Moving Averages)
market_data['ma_7'] = market_data['price'].rolling(window=7).mean()
market_data['ma_14'] = market_data['price'].rolling(window=14).mean()
market_data['momentum'] = market_data['ma_7'] - market_data['ma_14']

# Drop NaN values resulting from rolling calculations
market_data.dropna(inplace=True)

# Save the engineered features
market_data.to_csv('../../processed/market_features.csv', index=False)

print(market_data.head())
