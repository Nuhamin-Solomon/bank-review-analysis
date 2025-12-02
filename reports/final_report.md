# Interim Report: Bank Mobile App Review Analysis (Tasks 1–4)

**Author:** Nuhamin Solomon  
**Date:** December 2025  

---

## Overall Challenge

Scrape Google Play Store reviews for three Ethiopian banks (**CBE, BOA, Dashen**) and analyze customer satisfaction.  
The goal is to derive **data-driven insights** and suggest fintech app improvements.

---

## 1. Introduction

This report summarizes progress on analyzing customer reviews for three Ethiopian bank mobile applications: CBE, BOA, and Dashen.  
The objective is to identify **drivers of user satisfaction**, highlight **pain points**, and recommend actionable app improvements.

---

## 2. Task 1: Data Collection & Preprocessing

### 2.1 Scraping Reviews
- Collected ≥400 reviews per bank using Python (`google-play-scraper`).
- Captured fields: `review_text`, `rating`, `review_date`, `bank_name`, `app_name`, `source`.
- All scripts and datasets are version controlled in a dedicated Git branch (`task-1`/`task-2`).

### 2.2 Cleaning Data
- Removed duplicates and handled missing values (<5% of dataset).
- Normalized dates to **YYYY-MM-DD** format.
- Saved cleaned dataset as `cleaned_reviews.csv`.

### 2.3 Sample Cleaned Reviews

| Review | Rating | Date | Bank | Source |
|--------|-------|------|------|--------|
| the most advanced app. but how to stay safe? | 5 | 2025-11-28 | Dashen | Google Play |
| Good application | 4 | 2025-11-28 | CBE | Google Play |
| It is nice app | 5 | 2025-11-28 | BOA | Google Play |

---

## 3. Task 2: Sentiment & Thematic Analysis

### 3.1 Sentiment Analysis
- Used **VADER** to classify reviews as positive, neutral, or negative.
- Output dataset: `reviews_with_sentiment.csv`.

#### Sentiment Distribution (1,500 reviews total)

![Sentiment Distribution](../data/plots/sentiment_distribution.png)

| Sentiment | Count |
|-----------|-------|
| Positive  | 871   |
| Neutral   | 439   |
| Negative  | 190   |

**Observation:** Most reviews are positive, but negative reviews frequently mention login issues and slow transactions.

### 3.2 Thematic Analysis
- Extracted keywords using **spaCy** (nouns, proper nouns, adjectives).
- Grouped keywords into **3–5 themes per bank**:
  - Account Access Issues
  - Transaction Performance
  - User Interface & Experience
  - Customer Support
  - Features
- Output dataset: `reviews_with_themes.csv`.

#### Theme & Sentiment Visualizations per Bank

##### CBE
![CBE Theme Sentiment](../data/plots/CBE_theme_sentiment.png)

##### BOA
![BOA Theme Sentiment](../data/plots/BOA_theme_sentiment.png)

##### Dashen
![Dashen Theme Sentiment](../data/plots/Dashen_theme_sentiment.png)

**Observation:**  
- UI & Transaction Performance are the most frequent themes.  
- Dashen Bank receives more UI-related comments compared to CBE and BOA.

---

## 4. Task 3: PostgreSQL Integration

- Created database: `bank_reviews`
- **Banks Table:** `bank_id` (PK), `bank_name`, `app_name`  
- **Reviews Table:** `review_id` (PK), `bank_id` (FK), `review_text`, `rating`, `review_date`, `sentiment_label`, `sentiment_score`, `source`
- Inserted cleaned reviews via Python (`psycopg2`).
- Verified integrity with SQL queries:

```sql
SELECT COUNT(*) FROM reviews;
SELECT bank_id, COUNT(*) FROM reviews GROUP BY bank_id;
SELECT sentiment_label, COUNT(*) FROM reviews GROUP BY sentiment_label;
