
import pandas as pd
import numpy as np
#from alpha_vantage.timeseries import TimeSeries
import yfinance as yf

import streamlit as st
import Charts as ch
from dateutil.relativedelta import relativedelta

col1, col2, col3 = st.columns(3)
# Fetch live price (latest close price for the day)
# stock_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA","RY"]
time_duration = ["1W","1M","6M", "1Y", "3Y", "5Y", "ALL"]
stock_info_data = pd.read_csv("https://github.com/AdityaPhokmare/stockmarket_analysis/blob/main/Stock_Info.csv?raw=true", index_col=0)
stock_info_data.set_index("Name", inplace = True)
stock_info_data["Country"].fillna("Other", inplace = True)
stock_names_dict = stock_info_data["Symbol"].to_dict()
with col1:
    
    country_name = st.selectbox("Select Country Name :",stock_info_data["Country"].unique())

    available_stocks = stock_info_data[stock_info_data["Country"] == country_name]
    stock_name = st.selectbox("Stock Name :heavy_dollar_sign:",available_stocks.index.to_list())
    ticker_name = stock_names_dict[stock_name]
    
    stock = yf.Ticker(ticker_name)
    stock_data = stock.history(period="max")

    # stock_data, meta_data = ts.get_daily(symbol=stock_name, outputsize='full')
    stock_data.columns = [col.upper() for col in stock_data.columns]
    stock_data.index = pd.to_datetime(stock_data.index)
    stock_data.sort_index(inplace = True)
    

with col2:
    chart_switch = st.toggle("Switch Charts :chart:")
    customize_date = st.toggle("Customize Date :chart:")
    duration = st.selectbox("Duration :hourglass_flowing_sand:",time_duration, disabled=customize_date)

with col3:
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




