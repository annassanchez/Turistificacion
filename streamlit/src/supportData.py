import pandas as pd
import requests
import xmltodict
import json
import pickle
import fiona
import geopandas as gpd
pd.set_option('display.max_columns', None)
from IPython.display import clear_output

def importDatasets():
    df_2017 = gpd.read_file('../output/grid_2017.geojson').to_crs(epsg=4326)

    neighborhoods = gpd.read_file('../data/airbnb_airdna/2022_06_07/neighbourhoods.geojson').to_crs(epsg=4326)

    df_2023 = gpd.read_file('../output/grid_2023.geojson').to_crs(epsg=4326)

    gdf_2023 = neighborhoods.sjoin(df_2023, how="left")

    gdf_2017 = neighborhoods.sjoin(df_2017, how="left")

    return gdf_2017, gdf_2023

def importCompetenciaDelSuelo():
    gdf_2023 = gpd.read_file('../output/maps/grid_competencia_suelo_2023.geojson').to_crs(epsg=4326)
    gdf_2017 = gpd.read_file('../output/mapped/grid_competencia_suelo_2017.geojson').to_crs(epsg=4326)#[['fc_tot_offer', 'airbnb_tot_offer', 'abnb_tot_price', 'geometry']]
    return gdf_2017, gdf_2023