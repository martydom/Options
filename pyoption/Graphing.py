import plotly.graph_objects as go
from datetime import datetime

def candles(df,date = None):
    if date:
        x = df['Time']
    else:
        x = df['Date']
    fig = go.Figure(data=[go.Candlestick(
                    x=x,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])
    return fig