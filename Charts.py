import plotly.graph_objects as go
import datetime
from dateutil.relativedelta import relativedelta
def candlestick_chart(data, duration, stock_name, start_date = None, end_date = None):
    selected_data = custom_dates(data, duration, start_date, end_date)
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x = selected_data.index,
                                 close=selected_data["CLOSE"],
                                 high=selected_data["HIGH"],
                                 low=selected_data["LOW"],
                                 open=selected_data["OPEN"],
                                 increasing_line_color="green",
                                 decreasing_line_color="red",
                                 name="Candlestick",
                                 showlegend=True
                                ))
    
    # selected_data['50-day SMA'] = selected_data['CLOSE'].rolling(window=50).mean()
    # selected_data['200-day SMA'] = selected_data['CLOSE'].rolling(window=200).mean()

    # fig.add_trace(go.Scatter(
    #     x=selected_data.index,
    #     y=selected_data['50-day SMA'],
    #     mode='lines',
    #     name='50-day SMA',
    #     line=dict(color='blue', width=1)
    # ))

    # fig.add_trace(go.Scatter(
    #     x=selected_data.index,
    #     y=selected_data['200-day SMA'],
    #     mode='lines',
    #     name='200-day SMA',
    #     line=dict(color='orange', width=1)
    # ))
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_layout(title = f"{stock_name} Price (Daily Candlestick Chart)")
    fig.update_layout(xaxis=dict(title="<b>Date",showline=True,linewidth=2,linecolor="black"),
                      yaxis=dict(title="<b>Stock Price",showline=True,linewidth=2,linecolor="black"))
    fig.update_layout(width = 800, height = 400)
    return fig

def trend_chart(data,duration,stock_name,start_date=None,end_date=None):
    
    selected_data = custom_dates(data, duration, start_date, end_date)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x = selected_data["CLOSE"].index, y = selected_data["CLOSE"], mode = "lines + markers", marker=dict(size = 4), line=dict(color = "green")))
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)')
    #fig.update_layout(paper_bgcolor='rgba(0, 0, 0, 0)')
    fig.update_layout(title = f"{stock_name} Price (Daily Trend Chart)")

    fig.update_layout(xaxis=dict(title="<b>Date",showline=True,linewidth=2,linecolor="black"),
                      yaxis=dict(title="<b>Stock Price",showline=True,linewidth=2,linecolor="black"))

    fig.update_xaxes(showspikes=True,spikethickness = 1, spikecolor="black")
    fig.update_yaxes(showspikes=True,spikethickness = 1, spikecolor="black")
    fig.update_layout(width = 800, height = 400)
    return fig

def custom_dates(data, duration, start_date,end_date):
    if isinstance(start_date, str) or isinstance(end_date, str):
        selected_data = data.loc[start_date:end_date]
    
    if "W" in duration:
        selected_duration = data.index[-1] - relativedelta(weeks = 1)
        selected_data = data.loc[selected_duration:]
    elif "M" in duration:
        selected_duration = data.index[-1] - relativedelta(months = int(duration[0]))
        selected_data = data.loc[selected_duration:]
    elif "Y" in duration :
        selected_duration = data.index[-1] - relativedelta(years = int(duration[0]))
        selected_data = data.loc[selected_duration:]
    elif "ALL" in duration:
        selected_data = data

    return selected_data
