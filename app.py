
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Financial Data Trends Dashboard", page_icon="📈", layout="wide")

DATA = Path(__file__).parent / "financial_stock_data.csv"
df = pd.read_csv(DATA, parse_dates=["Date"])

st.title("📈 Financial Data Trends — Stock Analysis")
st.caption("Academic project dashboard: time-series trends, candlestick analysis, volume, and month-on-month performance.")

# Sidebar filters
st.sidebar.header("Filters")
tickers = sorted(df["Ticker"].unique())
selected = st.sidebar.multiselect("Select stock(s)", tickers, default=[tickers[0]])
if not selected:
    st.warning("Please select at least one stock.")
    st.stop()

min_date, max_date = df["Date"].min().date(), df["Date"].max().date()
date_range = st.sidebar.date_input("Date range", [min_date, max_date], min_value=min_date, max_value=max_date)

if len(date_range) == 2:
    start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
else:
    start, end = pd.Timestamp(min_date), pd.Timestamp(max_date)

d = df[df["Ticker"].isin(selected) & df["Date"].between(start, end)].copy()

# KPIs
latest = d.sort_values("Date").groupby("Ticker").tail(1)
first = d.sort_values("Date").groupby("Ticker").head(1)
total_return = ((latest.set_index("Ticker")["Close"] / first.set_index("Ticker")["Close"] - 1) * 100).mean()
avg_volume = d["Volume"].mean()
high_price = d["High"].max()
low_price = d["Low"].min()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Latest Close", f"₹{latest['Close'].mean():,.2f}")
c2.metric("Avg Return (selected)", f"{total_return:.2f}%")
c3.metric("Period High", f"₹{high_price:,.2f}")
c4.metric("Avg Daily Volume", f"{avg_volume:,.0f}")

# Price trend
st.subheader("1. Closing Price Trend")
fig = px.line(d, x="Date", y="Close", color="Ticker", title="Daily Closing Price")
fig.update_layout(hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)

# Candlestick
st.subheader("2. Candlestick Pattern")
candle_ticker = st.selectbox("Candlestick stock", selected)
cd = d[d["Ticker"] == candle_ticker].sort_values("Date")
fig2 = go.Figure(data=[go.Candlestick(
    x=cd["Date"], open=cd["Open"], high=cd["High"],
    low=cd["Low"], close=cd["Close"], name=candle_ticker
)])
fig2.update_layout(xaxis_rangeslider_visible=False, title=f"{candle_ticker} OHLC Candlestick")
st.plotly_chart(fig2, use_container_width=True)

# Monthly MoM
st.subheader("3. Month-on-Month Performance")
m = (d.sort_values("Date")
       .groupby(["Ticker", pd.Grouper(key="Date", freq="ME")], as_index=False)
       .agg(Month_End_Close=("Close","last"), Avg_Close=("Close","mean"), Volume=("Volume","sum")))
m["MoM_Return_%"] = m.groupby("Ticker")["Month_End_Close"].pct_change() * 100
fig3 = px.bar(m, x="Date", y="MoM_Return_%", color="Ticker", barmode="group",
              title="Month-on-Month Return (%)")
fig3.add_hline(y=0, line_width=1)
st.plotly_chart(fig3, use_container_width=True)

# Volume
st.subheader("4. Trading Volume")
fig4 = px.area(d, x="Date", y="Volume", color="Ticker", title="Daily Trading Volume")
st.plotly_chart(fig4, use_container_width=True)

# Summary table
st.subheader("5. Monthly Summary")
summary = m.copy()
summary["Date"] = summary["Date"].dt.strftime("%Y-%m")
st.dataframe(summary.round(2), use_container_width=True)

st.info("Note: The included dataset is simulated for academic/dashboard practice. Replace it with a real Kaggle dataset if your instructor requires real market observations.")
