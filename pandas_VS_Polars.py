import time
import pandas as pd
import polars as pl
import numpy as np

data = np.random.randint(0, 100, size=(120000, 3))
columns = ['A', 'B', 'C']

# Creating DataFrames
df_pandas = pd.DataFrame(data, columns=columns)
df_polars = pl.DataFrame(data)
df_polars.columns = columns  # Rename columns to match

def time_operation(df, operation):
    start_time = time.perf_counter()
    result = operation(df)
    end_time = time.perf_counter()
    return result, end_time - start_time

# Pandas and Polars operations
def pandas_read(df):
    return df

def polars_read(df):
    return df

_, pandas_time = time_operation(df_pandas, pandas_read)
_, polars_time = time_operation(df_polars, polars_read)

print(f"Reading: Pandas {pandas_time:.6f}s, Polars {polars_time:.6f}s")

def pandas_aggregate(df):
    return df.groupby('A').agg({'B': 'mean'})

def polars_aggregate(df):
    return df.group_by('A').agg(pl.col('B').mean())

_, pandas_time = time_operation(df_pandas, pandas_aggregate)
_, polars_time = time_operation(df_polars, polars_aggregate)

print(f"Aggregation: Pandas {pandas_time:.6f}s, Polars {polars_time:.6f}s")

def pandas_filter(df):
    return df[df['A'] > 50]

def polars_filter(df):
    return df.filter(pl.col('A') > 50)

_, pandas_time = time_operation(df_pandas, pandas_filter)
_, polars_time = time_operation(df_polars, polars_filter)

print(f"Filtering: Pandas {pandas_time:.6f}s, Polars {polars_time:.6f}s")

def pandas_join(df1, df2):
    return df1.merge(df2, on='A')

def polars_join(df1, df2):
    return df1.join(df2, on='A')

df_pandas2 = df_pandas.copy()
df_polars2 = df_polars.clone()

_, pandas_time = time_operation(df_pandas, lambda df: pandas_join(df, df_pandas2))
_, polars_time = time_operation(df_polars, lambda df: polars_join(df, df_polars2))

print(f"Joining: Pandas {pandas_time:.6f}s, Polars {polars_time:.6f}s")
