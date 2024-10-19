# run reddit scripts
cd reddit
python fetch_posts.py
python preprocess_data.py
python sentiment_analysis.py
cd ..

# #run crypto data scripts
cd crypto_data
python fetch_crypto_data.py
python feature_engineering.py
cd ..

# merge data daily
python merge_data_daily.py