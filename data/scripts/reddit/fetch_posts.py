import os
import praw
import pandas as pd
from dotenv import load_dotenv
import csv

# Load environment variables from .env
load_dotenv()

# Initialize PRAW with refresh token and other credentials
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    refresh_token=os.getenv('REDDIT_REFRESH_TOKEN'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

def fetch_reddit_posts(subreddit_name, limit=500):
    """
    Fetch recent posts from a subreddit.
    
    :param subreddit_name: Name of the subreddit to fetch posts from (e.g., "CryptoCurrency").
    :param limit: Maximum number of posts to fetch.
    :return: DataFrame containing posts data.
    """
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    
    for submission in subreddit.new(limit=limit):
        posts.append({
            'title': submission.title,
            'score': submission.score,
            'id': submission.id,
            'url': submission.url,
            'created': submission.created,
            'body': submission.selftext
        })
    
    return pd.DataFrame(posts)

# Example: Fetch posts from r/CryptoCurrency and save them as CSV
if __name__ == "__main__":
    df = fetch_reddit_posts('CryptoCurrency', limit=1000)
    df.to_csv('../../raw/reddit_crypto_posts.csv', index=False, quoting=csv.QUOTE_ALL, escapechar='\\')
    print(df.head())
