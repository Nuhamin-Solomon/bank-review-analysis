import pandas as pd
from pathlib import Path

# Paths
data_path = Path(__file__).parent.parent / "data"
raw_csv = data_path / "raw_reviews.csv"
clean_csv = data_path / "cleaned_reviews.csv"

# Load raw reviews
df = pd.read_csv(raw_csv)

# Remove duplicates
df = df.drop_duplicates(subset=["review", "date", "bank"])

# Handle missing values (avoid inplace to remove FutureWarning)
df["review"] = df["review"].fillna("No review text")
df["rating"] = df["rating"].fillna(df["rating"].median())

# Normalize dates
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Save cleaned dataset
df.to_csv(clean_csv, index=False)
print(f"Preprocessing completed! Saved cleaned dataset to {clean_csv}")
