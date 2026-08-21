# Automated Crypto Market BI Dashboard & Data Pipeline

An end-to-end, fully automated Data Engineering project that extracts real-time cryptocurrency market data, transforms and cleanses it, stores it in a cloud-hosted PostgreSQL database, and presents key performance metrics through an interactive Business Intelligence (BI) dashboard.

---

## Live Demo & Links

* **Live Dashboard:** [Crypto BI Dashboard](https://crypto-etl-dashboard-8hxhaajuxsfgd2lq8x2hqw.streamlit.app)
* **GitHub Repository:** [crypto-etl-dashboard](https://github.com/Harshit-Tiwary/crypto-etl-dashboard)

---

## System Architecture

```text
[ CoinGecko API ]
       │
       ▼  (Extraction)
[ Python ETL Script (etl.py) ]
       │
       ▼  (Transformation)
[ Pandas Data Cleaning & Normalization ]
       │
       ▼  (Loading)
[ Supabase PostgreSQL Database ]
       │
       ├──────────────────────────────┐
       ▼                              ▼
[ GitHub Actions Cron ]       [ Streamlit BI Dashboard ]
(Daily Automated Trigger)     (Real-time Visualization)
