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



