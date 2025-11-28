from google_play_scraper import Sort, reviews
import pandas as pd
from pathlib import Path

# Ensure data folder exists
data_path = Path("../data")
data_path.mkdir(exist_ok=True)

# Bank apps to scrape
apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():
    print(f"Scraping reviews for {bank}...")
    rvs, _ = reviews(
        app_id,
        lang="en",
        count=500,
        sort=Sort.NEWEST
    )

    for item in rvs:
        all_reviews.append({
            "review": item.get("content"),
            "rating": item.get("score"),
            "date": item.get("at"),
            "bank": bank,
            "source": "Google Play"
        })

# Save raw reviews to data folder
raw_csv = data_path / "raw_reviews.csv"
df = pd.DataFrame(all_reviews)
from pathlib import Path

# Create data folder path relative to this script
data_path = Path(__file__).parent.parent / "data"
data_path.mkdir(exist_ok=True)  # make sure it exists

# Save raw_reviews.csv to data folder
df.to_csv(data_path / "raw_reviews.csv", index=False)
print(f"Scraping completed! Saved to {data_path / 'raw_reviews.csv'}")

