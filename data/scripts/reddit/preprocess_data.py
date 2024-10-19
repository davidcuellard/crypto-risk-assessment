from textblob import TextBlob
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Load the dataset
df = pd.read_csv('../../raw/reddit_crypto_posts.csv')

# Function to preprocess text (both title and body)
def preprocess_text(text):
    if pd.isna(text):  # Handle missing text
        return ''

    text = text.replace('\n', ' ')
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    return ' '.join(tokens)

# Apply preprocessing to both the 'title' and 'body'
df['cleaned_title'] = df['title'].apply(preprocess_text)
df['cleaned_body'] = df['body'].apply(preprocess_text)

# Drop unnecessary columns and save the cleaned dataset
df.drop(columns=['title', 'body'], inplace=True)
df.to_csv('../../processed/cleaned_reddit_crypto_posts.csv', index=False)

print(df.head())