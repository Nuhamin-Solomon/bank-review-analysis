import pandas as pd
from pathlib import Path

# Set paths
data_path = Path("../data")
raw_csv = data_path / "raw_reviews.csv"
clean_csv = data_path / "cleaned_reviews.csv"

# Load raw reviews
df = pd.read_csv(raw_csv)

# Remove duplicates
df.drop_duplicates(subset=["review", "date", "bank"], inplace=True)

# Handle missing values
df["review"].fillna("No review text", inplace=True)
df["rating"].fillna(df["rating"].median(), inplace=True)

# Normalize date format
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Save cleaned dataset
df.to_csv(clean_csv, index=False)
print(f"Preprocessing completed! Saved cleaned dataset to {clean_csv}")
