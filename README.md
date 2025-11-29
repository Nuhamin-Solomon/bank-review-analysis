\# bank-review-analysis



Pipeline to scrape Google Play reviews for bank apps, preprocess text, compute sentiment and extract themes.



Folders:

\- `src/` : modular Python modules

\- `scripts/` : runnable scripts

\- `data/` : data outputs (ignored by git; put small samples in `data/samples/`)

\- `visualizations/` : plots

\- `sql/` : DB schema



Quick run:

1\. pip install -r requirements.txt

2\. python scripts\\scrape\_reviews.py

3\. python scripts\\preprocess\_reviews.py

4\. python scripts\\sentiment\_and\_themes.py
## Task 3 — Store Cleaned Data in PostgreSQL

- Database: bank_reviews
- Tables: banks, reviews
- CSV path: data/reviews_with_sentiment.csv
- Python script: scripts/insert_into_postgres.py
- Run:
  pip install psycopg2-binary pandas
  python scripts/insert_into_postgres.py



