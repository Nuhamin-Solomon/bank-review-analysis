import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load sentiment dataset
data_path = Path("data/reviews_with_sentiment.csv")
df = pd.read_csv(data_path)

print("Dataset loaded:", df.shape)

# Plot 1 — Sentiment distribution
plt.figure(figsize=(6,4))
df['sentiment_label'].value_counts().plot(kind="bar")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("data/plots/sentiment_distribution.png")

# Plot 2 — Reviews per bank
plt.figure(figsize=(6,4))
df['bank'].value_counts().plot(kind="bar")
plt.title("Reviews per Bank")
plt.xlabel("Bank")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("data/plots/reviews_per_bank.png")

print("Plots saved in data/plots/")
