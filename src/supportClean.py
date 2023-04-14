import numpy as np
import pandas as pd
from tqdm import tqdm
import os
from glob import glob

tqdm.pandas()
from IPython.display import clear_output

# geolocation
import geopy
import geopandas
from geopy.extra.rate_limiter import RateLimiter
from functools import partial
from geopy import Nominatim

import warnings
warnings.filterwarnings('ignore')

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
    """
    This code defines a function called geolocation that takes two arguments: 
        - a DataFrame (df) 
        - and a string column name (column). 
    The function uses the Nominatim geocoding service to convert location data in the specified column into latitude, longitude, and altitude coordinates.
    The steps taken by the function are as follows:
        - A RateLimiter object is created to limit the rate of geocoding requests sent to the Nominatim API.
        - A new column called location is created in the DataFrame using the progress_apply() method, which applies the geocode function (created in step 1) to each row of the specified column.
        - A new column called point is created in the DataFrame by applying a lambda function to the location column. 
    This lambda function extracts the point attribute from each Location object returned by the geocoding process.
    If no Location object is returned, the lambda function returns a tuple containing three None values (one for each of the coordinates).
        - The point column is split into three separate columns for latitude, longitude, and altitude using the tolist() and DataFrame methods from the Pandas library.
        - The resulting DataFrame is returned by the function, with the first row displayed using the head() method.
    """
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

def open_csvs_different_folders(root_folder, filename):
    """
    This function opens and reads multiple CSV files that are located in different folders under a root folder. It takes two arguments: 
        - `root_folder`, which is the path to the root folder containing the CSV files, 
        - and `file`, which is the name of the CSV file(s) to be read.
    The function first searches for all CSV files with the specified name (file) in all subdirectories under the root_folder. 
    It then reads each CSV file using pandas' read_csv method and appends the resulting DataFrame to a list df_list. 
    Finally, the function concatenates all DataFrames in df_list along the row axis (i.e., vertically) using pandas' concat method, removes any duplicate rows with drop_duplicates, and returns the resulting combined DataFrame.
    """
    all_csv_files = [file
                 for path, subdir, files in os.walk(root_folder)
                 for file in glob(os.path.join(path, filename))]
    df_list = []
    for file in all_csv_files:
        df_temp = pd.read_csv(file)
        df_list.append(df_temp)
    return pd.concat(df_list, axis = 0).drop_duplicates()