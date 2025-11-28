from google_play_scraper import Sort, reviews
import pandas as pd

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():
    r, _ = reviews(
        app_id,
        lang="en",
        count=500,
        sort=Sort.NEWEST
    )

    for item in r:
        all_reviews.append({
            "review": item.get("content"),
            "rating": item.get("score"),
            "date": item.get("at"),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)
df.to_csv("../data/raw_reviews.csv", index=False)
print("Saved raw_reviews.csv")
