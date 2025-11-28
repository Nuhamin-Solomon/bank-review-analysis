"""
Thematic Analysis Script
- Reads reviews with sentiment scores
- Extracts keywords using spaCy
- Groups keywords into 3-5 themes per bank
- Saves the results to CSV
"""

import pandas as pd
from pathlib import Path
import spacy
import re

# -----------------------------
# Step 1: Setup paths
# -----------------------------
data_path = Path(__file__).parent.parent / "data"
input_csv = data_path / "reviews_with_sentiment.csv"
output_csv = data_path / "reviews_with_themes.csv"

# -----------------------------
# Step 2: Load dataset
# -----------------------------
df = pd.read_csv(input_csv)
print(f"Loaded {len(df)} reviews from {input_csv}")

# -----------------------------
# Step 3: Initialize spaCy
# -----------------------------
nlp = spacy.load("en_core_web_sm")

# -----------------------------
# Step 4: Preprocess and extract keywords
# -----------------------------
def extract_keywords(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # remove punctuation
    doc = nlp(text)
    # Keep nouns, proper nouns, adjectives; remove stopwords
    keywords = [token.lemma_ for token in doc if token.pos_ in ('NOUN','PROPN','ADJ') and not token.is_stop]
    return keywords

df['keywords'] = df['review'].apply(extract_keywords)

# -----------------------------
# Step 5: Assign themes based on keywords (rule-based)
# -----------------------------
themes_dict = {
    'Account Access Issues': ['login','password','signin','account','locked'],
    'Transaction Performance': ['transfer','payment','slow','transaction','delay'],
    'User Interface & Experience': ['ui','design','interface','easy','navigation','app'],
    'Customer Support': ['support','help','customer','call','service'],
    'Features': ['feature','update','notification','option','function']
}

def assign_themes(keywords):
    assigned = []
    for theme, kw_list in themes_dict.items():
        if any(kw in keywords for kw in kw_list):
            assigned.append(theme)
    return assigned if assigned else ['Other']

df['themes'] = df['keywords'].apply(assign_themes)

# -----------------------------
# Step 6: Save results
# -----------------------------
df.to_csv(output_csv, index=False)
print(f"Saved thematic analysis results to {output_csv}")

# -----------------------------
# Step 7: Example output
# -----------------------------
print("\nExample themes per review:")
print(df[['review','themes']].head())
