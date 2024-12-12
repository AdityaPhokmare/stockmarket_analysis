
import pandas as pd
import numpy as np
#from alpha_vantage.timeseries import TimeSeries
import yfinance as yf

import streamlit as st
import Charts as ch
from dateutil.relativedelta import relativedelta
# api_key = "4K764NAX8K529PGF"
# ts = TimeSeries(key=api_key, output_format='pandas')
ticker_symbol = "AAPL"
col1, col2, col3 = st.columns(3)
# Fetch live price (latest close price for the day)
stock_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA"]
time_duration = ["1W","1M","6M", "1Y", "3Y", "5Y", "ALL"]
with col1:
    stock_name = st.selectbox("Stock Name :heavy_dollar_sign:",stock_symbols)
    stock = yf.Ticker(stock_name)
    stock_data = stock.history(period="max")

    # stock_data, meta_data = ts.get_daily(symbol=stock_name, outputsize='full')
    stock_data.columns = [col.upper() for col in stock_data.columns]
    stock_data.index = pd.to_datetime(stock_data.index)
    stock_data.sort_index(inplace = True)
    chart_switch = st.toggle("Switch Charts :chart:")
    

with col2:
    customize_date = st.toggle("Customize Date :chart:")

with col3:
    duration = st.selectbox("Duration :hourglass_flowing_sand:",time_duration, disabled=customize_date)
    if customize_date:
        duration = ""
    start_date,end_date = str(st.date_input("Start Date", disabled = not customize_date)), str(st.date_input("End Date", disabled = not customize_date))

    CandleStick = ch.candlestick_chart(data=stock_data,duration = duration,stock_name=stock_name,start_date=start_date,end_date=end_date)
    Trends = ch.trend_chart(data=stock_data,duration = duration,stock_name=stock_name,start_date=start_date,end_date=end_date)

if chart_switch:
    st.plotly_chart(Trends)
else:
    st.plotly_chart(CandleStick)


#     chart_name = st.selectbox("Chart Views :chart: ", ["CandleStick","Trends"])
# if chart_name == "CandleStick":st.plotly_chart(CandleStick)
# if chart_name == "Trends":st.plotly_chart(Trends)




