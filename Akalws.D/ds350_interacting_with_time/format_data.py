# %%
import polars as pl
import pandas as pd
import yfinance as yf

# %%
# We want this.
# ┌────────┬──────────────┬───────────┬───────────┬───────────┬───────────┬───────────┬──────────┐
# │ ticker ┆ date         ┆ Adj Close ┆ Close     ┆ High      ┆ Low       ┆ Open      ┆ Volume   │
# │ ---    ┆ ---          ┆ ---       ┆ ---       ┆ ---       ┆ ---       ┆ ---       ┆ ---      │
# │ str    ┆ datetime[ns] ┆ f64       ┆ f64       ┆ f64       ┆ f64       ┆ f64       ┆ f64      │
# ╞════════╪══════════════╪═══════════╪═══════════╪═══════════╪═══════════╪═══════════╪══════════╡
# │ CXW    ┆ 2019-01-25   ┆ 16.794144 ┆ 19.17     ┆ 19.360001 ┆ 18.959999 ┆ 19.280001 ┆ 496300.0 │
# │        ┆ 00:00:00     ┆           ┆           ┆           ┆           ┆           ┆          │
# │ CXW    ┆ 2019-01-28   ┆ 16.855467 ┆ 19.24     ┆ 19.360001 ┆ 18.889999 ┆ 19.120001 ┆ 621000.0 │
# │        ┆ 00:00:00     ┆           ┆           ┆           ┆           ┆           ┆          │
# │ CXW    ┆ 2019-01-29   ┆ 17.197132 ┆ 19.629999 ┆ 19.690001 ┆ 19.139999 ┆ 19.290001 ┆ 457800.0 │
# │        ┆ 00:00:00     ┆           ┆           ┆           ┆           ┆           ┆          │
# │ CXW    ┆ 2019-01-30   ┆ 17.144569 ┆ 19.57     ┆ 19.790001 ┆ 19.4      ┆ 19.629999 ┆ 534000.0 │
# │        ┆ 00:00:00     ┆           ┆           ┆           ┆           ┆           ┆          │
# │ CXW    ┆ 2019-01-31   ┆ 17.407389 ┆ 19.870001 ┆ 19.870001 ┆ 19.33     ┆ 19.58     ┆ 526000.0 │
# │        ┆ 00:00:00     ┆           ┆           ┆           ┆           ┆           ┆          │
# └────────┴──────────────┴───────────┴───────────┴───────────┴───────────┴───────────┴──────────┘
#%%

tickers_use = ["CXW", "F", "GM", "JCP", "KR", "WDC", "NKE", "T", "WDAY", "WFC", "WMT"]

# Download stock data for the last 5 years
dat = yf.download(tickers_use, period="5y", interval="1d").reset_index()
dat
#%%

# assuming the given pandas dataframe is stored in a variable named `dat`
dat = pl.from_pandas(dat).melt(id_vars="('Date', '')")\
    .with_columns(
        pl.col("variable")\
            .str.replace_many(["'", "(",")", " "], "")\
            .str.split_exact(",", 1).alias("variable"))\
    .unnest("variable")\
    .rename({"('Date', '')":"date"})\
    .pivot(
        values="value",
        index=["field_1","date"],
        columns="field_0",
        aggregate_function="first")\
    .rename({"field_1":"ticker"})
dat
#pdat.write_parquet("stock.parquet")

# %%
dat.write_parquet("stock.parquet")
# %%
