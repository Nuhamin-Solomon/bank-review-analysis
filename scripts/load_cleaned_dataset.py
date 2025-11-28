"""
Step 2: Load Cleaned Dataset
This script loads the cleaned reviews CSV from Task 1
and displays basic information to verify the data is ready
for sentiment and thematic analysis.
"""

# -----------------------------
# Step 2.3: Import Python libraries
# -----------------------------
import pandas as pd
from pathlib import Path

# -----------------------------
# Step 2.4: Define path to data folder
# -----------------------------
# The cleaned_reviews.csv is inside the 'data' folder
data_path = Path(__file__).parent.parent / "data"
clean_csv = data_path / "cleaned_reviews.csv"

# -----------------------------
# Step 2.5: Load the CSV into a DataFrame
# -----------------------------
df = pd.read_csv(clean_csv)

# -----------------------------
# Step 2.6: Inspect the dataset
# -----------------------------
# Display first 5 rows
print("First 5 reviews:")
print(df.head())

# Display DataFrame info (columns, types, missing values)
print("\nDataFrame info:")
print(df.info())

# Display total number of reviews
print(f"\nNumber of reviews loaded: {len(df)}")

# Optional: check number of reviews per bank
print("\nNumber of reviews per bank:")
print(df['bank'].value_counts())

# Optional: check number of reviews per rating
print("\nNumber of reviews per rating:")
print(df['rating'].value_counts())
