import pandas as pd
import requests
import xmltodict
import json
import pickle
import fiona
import geopandas as gpd
pd.set_option('display.max_columns', None)
from IPython.display import clear_output
import src.biblio as bb

def importDatasets():
    df_2017 = gpd.read_file('../output/grid_2017.geojson').to_crs(epsg=4326)

    neighborhoods = gpd.read_file('../data/airbnb_airdna/2022_06_07/neighbourhoods.geojson').to_crs(epsg=4326)

    df_2023 = gpd.read_file('../output/grid_2023.geojson').to_crs(epsg=4326)

    gdf_2023 = neighborhoods.sjoin(df_2023, how="left")

    gdf_2017 = neighborhoods.sjoin(df_2017, how="left")

    return gdf_2017, gdf_2023

def importCompetenciaDelSuelo():
    gdf_2023 = gpd.read_file('../output/maps/grid_competencia_suelo_2023.geojson').to_crs(epsg=4326)
    gdf_2017 = gpd.read_file('../output/maps/grid_competencia_suelo_2017.geojson').to_crs(epsg=4326)#[['fc_tot_offer', 'airbnb_tot_offer', 'abnb_tot_price', 'geometry']]
    return gdf_2017, gdf_2023

def importResiVSTouristDwellings():
    gdf_2023 = gpd.read_file('../output/maps/grid_sleep_2023.geojson').to_crs(epsg=4326)
    gdf_2017 = gpd.read_file('../output/maps/grid_sleep_2017.geojson').to_crs(epsg=4326)#[['fc_tot_offer', 'airbnb_tot_offer', 'abnb_tot_price', 'geometry']]
    return gdf_2017, gdf_2023

def importFiesta():
    gdf_2023 = gpd.read_file('../output/maps/grid_fiesta_2023.geojson').to_crs(epsg=4326)
    gdf_2017 = gpd.read_file('../output/maps/grid_fiesta_2017.geojson').to_crs(epsg=4326)#[['fc_tot_offer', 'airbnb_tot_offer', 'abnb_tot_price', 'geometry']]
    return gdf_2017, gdf_2023

def differenceGrids(grid_2017, grid_2023):
    df = pd.merge(grid_2017, grid_2023, on='neighbourhood', suffixes= ['_2017', '_2023'])
    columns_2017 = []
    for column in df.columns:
        if '_2017' in column and 'neighbourhood' not in column and 'geometry' not in column:
            columns_2017.append(column)
        else:
            continue
    columns_2023 = []
    for column in df.columns:
        if '_2023' in column and 'neighbourhood' not in column and 'geometry' not in column:
            columns_2023.append(column)
        else:
            continue
    new_cols = []
    for i, (old_col, new_col) in enumerate(zip(columns_2017, columns_2023)):
        new_col_name = f'{old_col}_{i}'
        new_col_ratio = f'{old_col}_ratio'
        df[new_col_name] = df[old_col] - df[new_col]
        df[new_col_ratio] = (df[new_col] - df[old_col]) / df[new_col] 
        new_cols.append(new_col_name)
    return df

def replaceFunction(string):
    if string in bb.fiesta:
        #print(bb.fiesta[key])
        return bb.fiesta[string]
    return string