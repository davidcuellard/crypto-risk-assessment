from textblob import TextBlob
import pandas as pd

# Load the preprocessed data
df = pd.read_csv('../../processed/cleaned_reddit_crypto_posts.csv')

# Convert 'created' to datetime if not already done
df['created'] = pd.to_datetime(df['created'], unit='s')
df['date'] = df['created'].dt.date

# Function to calculate sentiment polarity
def analyze_sentiment(text):
    if pd.isna(text) or text == '': 
        return 0.0  
    analysis = TextBlob(str(text))  
    return analysis.sentiment.polarity  

# Apply sentiment analysis to both the 'cleaned_title' and 'cleaned_body'
df['title_sentiment'] = df['cleaned_title'].apply(analyze_sentiment)
df['body_sentiment'] = df['cleaned_body'].apply(analyze_sentiment)

# Function to calculate combined sentiment based on conditions
def combined_sentiment(row):
    title_sentiment = row['title_sentiment']
    body_sentiment = row['body_sentiment']
    
    if title_sentiment == 0 and body_sentiment == 0:
        return 0.0  # If both are 0, return 0
    elif title_sentiment == 0:
        return body_sentiment  # If title sentiment is 0, use body sentiment
    elif body_sentiment == 0:
        return title_sentiment  # If body sentiment is 0, use title sentiment
    else:
        return (title_sentiment + body_sentiment) / 2  # Average if both are non-zero

# Apply the function to calculate the combined sentiment
df['combined_sentiment'] = df.apply(combined_sentiment, axis=1)

# **Aggregate Sentiment Data Daily**
# Group by date to get daily average sentiment
daily_sentiment = df.groupby('date')['combined_sentiment'].mean().reset_index()
daily_sentiment.rename(columns={'combined_sentiment': 'avg_sentiment'}, inplace=True)

# Save the individual sentiment scores
df.to_csv('../../processed/reddit_crypto_sentiment.csv', index=False)

# Save the daily aggregated sentiment scores
daily_sentiment.to_csv('../../processed/daily_sentiment.csv', index=False)

print("Individual sentiment data saved to 'reddit_crypto_sentiment.csv'")
print("Daily aggregated sentiment data saved to 'daily_sentiment.csv'")

print(df.head())
