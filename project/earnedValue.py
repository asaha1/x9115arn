import pandas

from contextlib import contextmanager
from numpy.core.numeric import arange

@contextmanager
def columns_in(df):
    col_names = df.columns
    col_list = [df[col] for col in col_names]
    try:
        yield tuple(col_list)
    finally:
        for i, col in enumerate(col_names):
            df[col] = col_list[i]
            
