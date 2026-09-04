# Project Requirement Checklist

| Requirement | Status | Evidence |
|---|---|---|
| Visualize financial trends over time | ✅ | Daily closing-price line chart |
| Stock-price analysis | ✅ | OHLCV stock dataset |
| Line charts | ✅ | Closing-price trend |
| Candlestick patterns | ✅ | Interactive OHLC candlestick in `app.py` |
| Area plots | ✅ | Trading-volume area chart |
| Month-on-month comparison | ✅ | `MoM_Return_%` + bar chart |
| Time-series analysis | ✅ | Date-based daily and monthly analysis |
| Forecasting (optional) | 🟡 Optional | Can be added in Power BI Analytics pane |
| Interactive filtering | ✅ | Stock and date filters in Streamlit; slicers in Power BI |
| Business/investment decision insight | ✅ | Trend, return, high/low and volume KPIs |
| Data cleaning/transformation | ✅ | Date parsing, return calculation, monthly aggregation |
| Power BI compatible | ✅ | CSV files + DAX guide |

## Dataset source option
A Kaggle alternative is:
https://www.kaggle.com/datasets/prodzar/stocks-historical-price-data

That dataset contains historical stock prices with Date, Open, High, Low, Close, Volume, Dividends and Stock Splits. If you replace the included simulated CSV with Kaggle data, map its columns to the dashboard fields.

Microsoft also provides an official Financial Sample workbook for Power BI:
https://learn.microsoft.com/en-us/power-bi/create-reports/sample-financial-download
