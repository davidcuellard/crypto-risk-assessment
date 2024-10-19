import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load market data
market_data = pd.read_csv('../processed/market_features.csv')

# Convert 'timestamp' to datetime
market_data['timestamp'] = pd.to_datetime(market_data['timestamp'])
market_data['date'] = market_data['timestamp'].dt.date
market_data['date'] = pd.to_datetime(market_data['date'])

# Load daily sentiment data
daily_sentiment = pd.read_csv('../processed/daily_sentiment.csv')
daily_sentiment['date'] = pd.to_datetime(daily_sentiment['date'])

# Merge market data with daily sentiment
final_data = pd.merge(market_data, daily_sentiment, on='date', how='left')

# Corrected Line: Fill missing sentiment values
final_data['avg_sentiment'] = final_data['avg_sentiment'].fillna(0.0)

# Ensure final_data is sorted by date
final_data.sort_values('date', inplace=True)
final_data.reset_index(drop=True, inplace=True)

# Create future price column by shifting 'price' backward
final_data['future_price'] = final_data['price'].shift(-1)

# Calculate future return
final_data['future_return'] = (final_data['future_price'] - final_data['price']) / final_data['price']

# Define risk_label based on future_return
final_data['risk_label'] = final_data['future_return'].apply(lambda x: 1 if x < 0 else 0)

# Drop the last row with NaN values
final_data.dropna(subset=['future_return'], inplace=True)

# Exclude 'price_return' from features to prevent data leakage
feature_columns = ['volatility', 'liquidity', 'momentum', 'avg_sentiment']
X = final_data[feature_columns]

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert back to DataFrame
X_scaled = pd.DataFrame(X_scaled, columns=feature_columns)

# Save scaled features
X_scaled.to_csv('../processed/model_features.csv', index=False)

# Save the target variable
target = final_data['risk_label']
target.to_csv('../processed/model_target.csv', index=False)

# Save the final dataset for reference
final_data.to_csv('../processed/final_dataset.csv', index=False)

print("Data processing complete. Features and target saved.")
