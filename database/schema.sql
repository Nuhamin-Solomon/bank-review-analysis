-- ==============================================
-- Safe PostgreSQL Script: Create Tables + Insert Banks
-- ==============================================

-- Drop tables if they exist
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS banks;

-- Create banks table
CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(50) NOT NULL UNIQUE,
    app_name VARCHAR(100)
);

-- Create reviews table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    review_text TEXT,
    rating INT,
    review_date DATE,
    sentiment_label VARCHAR(20),
    sentiment_score NUMERIC,
    source VARCHAR(50)
);

-- Insert banks (avoid duplicates)
INSERT INTO banks (bank_name, app_name)
VALUES 
    ('CBE', 'CBE Mobile Banking'),
    ('BOA', 'Bank of Abyssinia App'),
    ('Dashen', 'Dashen Mobile Banking')
ON CONFLICT (bank_name) DO NOTHING;
