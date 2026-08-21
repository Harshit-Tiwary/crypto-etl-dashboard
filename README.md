# Crypto Market BI Dashboard & Automated Data Pipeline

An end-to-end Data Engineering pipeline that extracts real-time cryptocurrency market metrics, cleanses and transforms the data, loads it into a cloud-hosted PostgreSQL instance, and visualizes insights on an interactive Business Intelligence dashboard.

---

## Live Links

* **Live Dashboard:** [Streamlit Web App](https://crypto-etl-dashboard-8hxhaajuxsfgd2lq8x2hqw.streamlit.app)
* **GitHub Repository:** [Source Code](https://github.com/Harshit-Tiwary/crypto-etl-dashboard)

---

## Architecture Flow

[ CoinGecko API ] ──(Extract)──> [ Python ETL Script ] ──(Transform)──> [ Pandas Data Cleaning ]
                                                                                   │
                                                                                (Load)
                                                                                   ▼
[ Streamlit BI Dashboard ] <──(Query)── [ Supabase PostgreSQL ] <──(Trigger)── [ GitHub Actions Cron ]

---

## Key Features

* **Automated Data Extraction:** Fetches top 20 cryptocurrencies by market capitalization via CoinGecko REST API.
* **Data Processing:** Cleans missing entries, formats timestamps, and normalizes financial metrics using Pandas.
* **Cloud Data Warehouse:** Persists structured records into Supabase PostgreSQL using SQLAlchemy.
* **Automated Workflow:** Uses GitHub Actions CI/CD to execute daily ETL runs automatically.
* **Interactive Dashboard:** Built with Streamlit to present KPI metrics, custom filters, and market distributions.

---

## Tech Stack

* **Language:** Python 3.10
* **Data Processing:** Pandas
* **Database & ORM:** PostgreSQL (Supabase Cloud), SQLAlchemy, Psycopg2
* **Automation & CI/CD:** GitHub Actions
* **Visualization:** Streamlit
* **Deployment:** Streamlit Community Cloud

---

## Repository Structure

crypto-etl-dashboard/
├── .github/
│   └── workflows/
│       └── etl_pipeline.yml    # Daily CI/CD automation workflow
├── app.py                      # Streamlit dashboard application
├── etl.py                      # Extraction, Transformation & Loading script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

---

## Local Setup Instructions

1. Clone the Repository:
   git clone https://github.com/Harshit-Tiwary/crypto-etl-dashboard.git
   cd crypto-etl-dashboard

2. Set Up Virtual Environment:
   python -m venv venv
   .\venv\Scripts\activate

3. Install Dependencies:
   pip install -r requirements.txt

4. Run Pipeline & Dashboard:
   python etl.py
   streamlit run app.py

---

## Author

* **Harshit Tiwary** - [GitHub Profile](https://github.com/Harshit-Tiwary)
