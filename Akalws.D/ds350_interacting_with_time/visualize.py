# %%
import polars as pl
import pandas as pd
import plotly.express as px

import plotly.graph_objects as go
from datetime import datetime
from lets_plot import *
import lets_plot as lp
LetsPlot.setup_html()

# %%
pdat = pl.read_parquet("stock.parquet")

#%%
performance_chart = px.line(pdat, x='date', y='Close', color='ticker',
                      title='Stock Performances Over the Last 5 Years',
                      labels={'date': 'Date', 'Close': 'Closing Price'})
performance_chart.show()


#%%


volume_chart = px.scatter(pdat, x='date', y='Volume', color='ticker',
             title='Volume of Stocks Over the Last 5 Years',
             labels={'date': 'Date', 'Volume': 'Volume'},
             category_orders={"ticker": ["CXW", "F", "GM", "JCP", "KR", "WDC", "NKE", "T", "WDAY", "WFC", "WMT"]},
             height=400, width=800)


volume_chart.show()

# %%
# now fix the html size and only show the last year and save the chart

# %%
## plotly candlestick chart
# https://plotly.com/python/candlestick-charts/

