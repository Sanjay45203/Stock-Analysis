# Financial Data Trends (Stock Analysis)

## Objective
Visualize and analyze time-based stock-price trends for smarter business/investment decisions.

## What is included
- `financial_stock_data.csv` — daily OHLCV dataset for 5 stocks, 2023–2025.
- `monthly_stock_summary.csv` — monthly summary and MoM return.
- `app.py` — interactive Streamlit dashboard that runs in VS Code.
- `requirements.txt` — Python packages.
- `POWER_BI_GUIDE.md` — exact Power BI dashboard build instructions.
- `PROJECT_CHECKLIST.md` — requirement-by-requirement verification.

## Important dataset note
The included dataset is **simulated academic data**, generated with a fixed random seed so the results are reproducible. It is not presented as actual market data.

If your instructor specifically requires Kaggle data, a suitable alternative is the Kaggle **Stocks Historical Price Data** dataset, which contains Date, Open, High, Low, Close, Volume, Dividends and Stock Splits. See the source listed in the project checklist.

## Run in VS Code
1. Open this folder in VS Code.
2. Open Terminal.
3. Create a virtual environment:
   `python -m venv .venv`
4. Activate it on Windows:
   `.venv\Scripts\activate`
5. Install packages:
   `pip install -r requirements.txt`
6. Run:
   `streamlit run app.py`
7. A browser page will open with the interactive dashboard.

## Power BI
Use `financial_stock_data.csv` as the main table. Follow `POWER_BI_GUIDE.md` for the visuals and DAX measures.
