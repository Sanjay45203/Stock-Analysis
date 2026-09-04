# Power BI Dashboard Guide

## Import
Power BI Desktop → Get Data → Text/CSV → `financial_stock_data.csv` → Load.

## Recommended data types
- Date: Date
- Ticker, Sector, Month, Month_Name: Text
- Open, High, Low, Close: Decimal number
- Volume: Whole number
- Daily_Return_%: Decimal number

## DAX measures
Create these measures in the stock data table:

```DAX
Total Trading Volume = SUM(financial_stock_data[Volume])

Average Close = AVERAGE(financial_stock_data[Close])

Maximum Price = MAX(financial_stock_data[High])

Minimum Price = MIN(financial_stock_data[Low])

Latest Close =
VAR LastDate = MAX(financial_stock_data[Date])
RETURN
CALCULATE(
    AVERAGE(financial_stock_data[Close]),
    financial_stock_data[Date] = LastDate
)

Average Daily Return = AVERAGE(financial_stock_data[Daily_Return_%])
```

For a clean MoM visual, also import `monthly_stock_summary.csv` as a second table.

## Dashboard layout
### Page 1 — Executive Overview
1. KPI Card: Latest Close
2. KPI Card: Average Close
3. KPI Card: Maximum Price
4. KPI Card: Total Trading Volume
5. Line chart: Date → Close; Legend → Ticker
6. Area chart: Date → Volume; Legend → Ticker
7. Slicers: Ticker, Sector, Date

### Page 2 — Detailed Trend Analysis
1. Candlestick/custom OHLC visual (or use Open/High/Low/Close with a suitable marketplace visual).
2. Line chart: Month_Start → Month_End_Close
3. Column chart: Month_Start → MoM_Return_%; Legend → Ticker
4. Table: Ticker, Month_Start, Month_End_Close, MoM_Return_%, Total_Volume

## Suggested dashboard title
"Financial Data Trends — Stock Performance Analysis"

## Interpretation examples
- Positive MoM return indicates the stock's month-end close increased relative to the previous month.
- Negative MoM return indicates a month-over-month decline.
- A rising closing-price line indicates an upward price trend over the selected period.
- Volume spikes can be investigated alongside sharp price movements.

## Optional forecasting
Power BI's Analytics pane can be used on a line chart to add a forecast when the required conditions are met. Forecasting is optional in the project statement.
