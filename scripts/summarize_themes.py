"""
Summarize Themes per Bank
- Reads reviews with themes
- Counts number of reviews per theme for each bank
- Optionally, plots a bar chart
"""

import pandas as pd
from pathlib import Path
import ast
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Setup paths
# -----------------------------
data_path = Path(__file__).parent.parent / "data"
input_csv = data_path / "reviews_with_themes.csv"

# -----------------------------
# Step 2: Load dataset
# -----------------------------
df = pd.read_csv(input_csv)
print(f"Loaded {len(df)} reviews from {input_csv}")

# Convert string representation of list back to actual list
df['themes'] = df['themes'].apply(ast.literal_eval)

# -----------------------------
# Step 3: Explode themes
# -----------------------------
# Each theme in a separate row to count them properly
df_exploded = df.explode('themes')

# -----------------------------
# Step 4: Count themes per bank
# -----------------------------
theme_counts = df_exploded.groupby(['bank','themes']).size().reset_index(name='count')
print("\nTheme counts per bank:")
print(theme_counts)

# -----------------------------
# Step 5: Optional: Plot bar charts
# -----------------------------
for bank in df['bank'].unique():
    bank_data = theme_counts[theme_counts['bank'] == bank]
    plt.figure(figsize=(8,5))
    plt.bar(bank_data['themes'], bank_data['count'], color='skyblue')
    plt.title(f"Theme Distribution for {bank}")
    plt.ylabel("Number of Reviews")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
