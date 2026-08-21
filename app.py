import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

st.set_page_config(page_title="Crypto Automated BI Dashboard", page_icon="🚀", layout="wide")

st.title("🚀 Automated Crypto Market BI Dashboard")
st.markdown("Real-time automated data pipeline refreshed daily via **GitHub Actions** & stored in **Supabase PostgreSQL**.")

DATABASE_URL = os.getenv("DATABASE_URL")

@st.cache_data(ttl=1800)
def get_data():
    if not DATABASE_URL:
        st.error("DATABASE_URL environment variable is missing!")
        return pd.DataFrame()
    
    db_url = DATABASE_URL
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
        
    engine = create_engine(db_url)
    df = pd.read_sql("SELECT * FROM top_crypto", engine)
    return df

try:
    df = get_data()

    if not df.empty:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Cryptos Tracked", len(df))
        col2.metric("Market Leader", df.iloc[0]['name'] if len(df) > 0 else "N/A")
        
        top_gainer = df.loc[df['price_change_percentage_24h'].idxmax()]
        col3.metric("Top Gainer (24h)", f"{top_gainer['symbol'].upper()}", f"{top_gainer['price_change_percentage_24h']:.2f}%")
        
        last_updated_str = pd.to_datetime(df['last_updated'].iloc[0]).strftime("%d %b %Y, %H:%M UTC")
        col4.metric("Last Updated", last_updated_str)

        st.markdown("---")

        search = st.text_input("🔍 Search Crypto by Name or Symbol:", "")
        filtered_df = df.copy()
        if search:
            filtered_df = filtered_df[
                filtered_df['name'].str.contains(search, case=False) | 
                filtered_df['symbol'].str.contains(search, case=False)
            ]

        col_left, col_right = st.columns(2)

        with col_left:
            st.subheader("Top 10 Cryptos by Market Cap (USD)")
            top10 = filtered_df.nlargest(10, 'market_cap')
            st.bar_chart(data=top10, x='name', y='market_cap', use_container_width=True)

        with col_right:
            st.subheader("24h Price Change (%)")
            st.bar_chart(data=filtered_df.head(10), x='name', y='price_change_percentage_24h', use_container_width=True)

        st.subheader("📊 Detailed Market Data Table")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.warning("Database me data abhi tak load nahi hua hai. ETL script run karein.")

except Exception as e:
    st.error(f"Error loading dashboard data: {e}")