import numpy as np
import pandas as pd
from tqdm import tqdm

tqdm.pandas()
from IPython.display import clear_output

# geolocation
import geopy
import geopandas
from geopy.extra.rate_limiter import RateLimiter
from functools import partial
from geopy import Nominatim


def columnList(dataframe, condition):
    """
    This function takes a dataframe and returns the columns that fulfill a condition
    args: - dataframe: the dataframe you want to slice the columns
        - condition: as a string
    returns:
        the column as a list that fulfill that conditions
    """
    column_list = []
    for columna in dataframe.columns:
        if condition in columna:
            column_list.append(columna)
        else:
            pass
    print(f'the columns that have {condition} on their name are:', column_list)
    return column_list

def geolocation(df, column):
    locator = Nominatim(user_agent="myGeocoder")

    # 1 - conveneint function to delay between geocoding calls
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
    # 2- - create location column
    try:
        df['location'] = df[column].progress_apply(geocode)
    except:
        clear_output(wait=True)
        pass
    # 3 - create longitude, laatitude and altitude from location column (returns tuple)
    df['point'] = df['location'].progress_apply(lambda loc: tuple(loc.point) if loc else (None, None, None))
    # 4 - split point column into latitude, longitude
    df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
    clear_output(wait=True)
    df.head(1)
    return df