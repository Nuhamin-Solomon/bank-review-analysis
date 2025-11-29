"""
Task 2: Sentiment Analysis
This script loads cleaned reviews from Task 1,
computes sentiment scores using VADER, and saves results to CSV.
"""

# -----------------------------
# Step 3.3: Import libraries
# -----------------------------
import pandas as pd
from pathlib import Path
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon (run once)
nltk.download('vader_lexicon')

# -----------------------------
# Step 3.4: Load cleaned dataset
# -----------------------------
data_path = Path(__file__).parent.parent / "data"
clean_csv = data_path / "cleaned_reviews.csv"

df = pd.read_csv(clean_csv)
print(f"Loaded {len(df)} reviews from {clean_csv}")

# -----------------------------
# Step 3.5: Initialize VADER
# -----------------------------
sia = SentimentIntensityAnalyzer()

# Compute sentiment score for each review
df['sentiment_score'] = df['review'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

# Convert compound score to label
df['sentiment_label'] = df['sentiment_score'].apply(
    lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral')
)

print("Sentiment analysis completed!")

# -----------------------------
# Step 3.6: Inspect results
# -----------------------------
print("\nSentiment distribution:")
print(df['sentiment_label'].value_counts())

print("\nExample reviews with sentiment:")
print(df[['review', 'sentiment_label', 'sentiment_score']].head())

# -----------------------------
# Step 3.7: Save results
# -----------------------------
output_csv = data_path / "reviews_with_sentiment.csv"
df.to_csv(output_csv, index=False)
print(f"Saved sentiment analysis results to {output_csv}")
