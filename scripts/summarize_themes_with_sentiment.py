"""
Summarize Themes per Bank with Sentiment
- Reads reviews with themes and sentiment_label
- Counts number of reviews per theme for each bank, split by sentiment
- Plots bar charts showing theme distribution by sentiment
- Saves plots as PNG files in the data folder
"""

import pandas as pd
from pathlib import Path
import ast
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Step 1: Setup paths
# -----------------------------
data_path = Path(__file__).parent.parent / "data"
input_csv = data_path / "reviews_with_themes.csv"
plots_path = data_path / "plots"
plots_path.mkdir(exist_ok=True)  # create folder if it doesn't exist

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
df_exploded = df.explode('themes')

# -----------------------------
# Step 4: Count reviews per theme per bank per sentiment
# -----------------------------
theme_sentiment_counts = (
    df_exploded
    .groupby(['bank','themes','sentiment_label'])
    .size()
    .reset_index(name='count')
)

print("\nTheme counts per bank with sentiment:")
print(theme_sentiment_counts)

# -----------------------------
# Step 5: Plot bar charts per bank and save
# -----------------------------
sns.set(style="whitegrid")

for bank in df['bank'].unique():
    bank_data = theme_sentiment_counts[theme_sentiment_counts['bank'] == bank]
    plt.figure(figsize=(10,6))
    sns.barplot(x='themes', y='count', hue='sentiment_label', data=bank_data)
    plt.title(f"Theme Distribution by Sentiment for {bank}")
    plt.ylabel("Number of Reviews")
    plt.xlabel("Theme")
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Sentiment')
    plt.tight_layout()
    
    # Save the plot
    plot_file = plots_path / f"{bank}_theme_sentiment.png"
    plt.savefig(plot_file)
    print(f"Saved plot for {bank} to {plot_file}")
    
    # Optional: close the figure to free memory
    plt.close()
