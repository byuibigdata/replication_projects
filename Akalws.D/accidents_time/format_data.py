# %%


import plotly.graph_objects as go
from datetime import datetime
from lets_plot import *
LetsPlot.setup_html()
import polars as pl
import pins
import pandas as pd
# %%
#%%
'''dat = pl.read_csv('https://data.cityofnewyork.us/resource/h9gi-nx95.csv?$query=SELECT%0A%20%20%60crash_date%60%2C%0A%20%20%60crash_time%60%2C%0A%20%20%60borough%60%2C%0A%20%20%60zip_code%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60longitude%60%2C%0A%20%20%60location%60%2C%0A%20%20%60on_street_name%60%2C%0A%20%20%60off_street_name%60%2C%0A%20%20%60cross_street_name%60%2C%0A%20%20%60number_of_persons_injured%60%2C%0A%20%20%60number_of_persons_killed%60%2C%0A%20%20%60number_of_pedestrians_injured%60%2C%0A%20%20%60number_of_pedestrians_killed%60%2C%0A%20%20%60number_of_cyclist_injured%60%2C%0A%20%20%60number_of_cyclist_killed%60%2C%0A%20%20%60number_of_motorist_injured%60%2C%0A%20%20%60number_of_motorist_killed%60%2C%0A%20%20%60contributing_factor_vehicle_1%60%2C%0A%20%20%60contributing_factor_vehicle_2%60%2C%0A%20%20%60contributing_factor_vehicle_3%60%2C%0A%20%20%60contributing_factor_vehicle_4%60%2C%0A%20%20%60contributing_factor_vehicle_5%60%2C%0A%20%20%60collision_id%60%2C%0A%20%20%60vehicle_type_code1%60%2C%0A%20%20%60vehicle_type_code2%60%2C%0A%20%20%60vehicle_type_code_3%60%2C%0A%20%20%60vehicle_type_code_4%60%2C%0A%20%20%60vehicle_type_code_5%60')\
     .with_columns(
         pl.col("CRASH DATE").str.to_date("%m/%d/%Y").alias("date"),
         pl.col("CRASH TIME").str.to_time("%H:%M").alias("time"),
         pl.concat_str(["CRASH DATE","CRASH TIME"], separator=" ")\
             .str.to_datetime("%m/%d/%Y %H:%M").alias("date_time"))

dat.write_parquet("ny_crashes.parquet", compression="zstd", compression_level=15)'''
# %%
dat = pl.read_parquet("ny_crashes.parquet")
dat

#%%
rates_hour=dat\
    .with_columns(
        pl.col('date_time').dt.truncate('1h').alias('hour_floor'))\
        .group_by('hour_floor')\
        .agg(
            pl.sum("NUMBER OF PERSONS INJURED").alias('injured_total'),
            pl.count('BOROUGH').alias('accidents'))\
        .with_columns(
        pl.col('hour_floor').dt.hour().alias('hour')
        )
rates_hour
#%%
rates_day=dat\
    .with_columns(
        pl.col('date_time').dt.truncate('1d').alias('day_floor'))\
        .group_by('day_floor')\
        .agg(
            pl.sum("NUMBER OF PERSONS INJURED").alias('injured_total'),
            pl.count('BOROUGH').alias('accidents'))\
    .with_columns(
        pl.col('day_floor').dt.weekday().alias('weekday')
        )
rates_day
#%%
ggplot(rates_day.sort('weekday'), aes(x = 'weekday', y = 'accidents')) +\
  geom_boxplot() +\
  scale_x_discrete()
#%%
# time series plot
'''ggplot(rates_hour, aes(x='hour', y='accidents')) +\
 geom_bar(stat='identity') +\
 scale_x_discrete()+\
 ggtitle("Number of accidents per hour")+\
theme(axis_text_x=element_text(angle=0, vjust=1))'''


(ggplot(rates_hour, aes(x='hour', y='accidents')) +
 geom_histogram(stat='identity', bins=len(rates_hour['hour'].unique()), fill= '#87CEEB') +
 scale_x_discrete() +
 ggtitle("Number of accidents per hour") +
 theme(axis_text_x=element_text(angle=0, vjust=0.5)))
# %%
# Now we want to create two visuals: the number of chrashes per hour and one that shows the number of injuries per day

# %%

# %%
