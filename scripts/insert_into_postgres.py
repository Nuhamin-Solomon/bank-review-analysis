import pandas as pd
import psycopg2
from pathlib import Path

# Load CSV
data_path = Path(__file__).parent.parent / "data" / "reviews_with_sentiment.csv"
df = pd.read_csv(data_path)
print(f"Loaded {len(df)} reviews")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="Kifiya@123",  # Replace with your PostgreSQL password
    port=5432
)
cursor = conn.cursor()

# Insert query
insert_query = """
INSERT INTO reviews
(bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, source)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# Map bank names to bank_id
bank_map = {"CBE": 1, "BOA": 2, "Dashen": 3}

# Insert rows
for _, row in df.iterrows():
    cursor.execute(insert_query, (
        bank_map[row['bank']],
        row['review'],
        row.get('rating', None),
        row.get('date', None),
        row['sentiment_label'],
        row['sentiment_score'],
        "Google Play"
    ))

conn.commit()
cursor.close()
conn.close()
print("Inserted all reviews into PostgreSQL!")
