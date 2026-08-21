import os
import pandas as pd
import requests
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 20, 'page': 1, 'sparkline': False}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def transform_data(data):
    if not data:
        return pd.DataFrame()
    df = pd.DataFrame(data)
    columns_to_keep = ['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h', 'last_updated']
    df = df[columns_to_keep]
    df['price_change_percentage_24h'] = df['price_change_percentage_24h'].fillna(0)
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    return df

def load_to_db(df):
    if df.empty:
        print("No data available to load.")
        return
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable is not set!")

    db_url = DATABASE_URL
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    try:
        engine = create_engine(db_url)
        df.to_sql("top_crypto", engine, if_exists="replace", index=False)
        print("ETL Pipeline executed successfully! Data pushed to Supabase PostgreSQL.")
    except Exception as e:
        print(f"Failed to load data into PostgreSQL database: {e}")

if __name__ == "__main__":
    print("Starting Crypto ETL Pipeline...")
    raw_data = fetch_crypto_data()
    cleaned_df = transform_data(raw_data)
    load_to_db(cleaned_df)