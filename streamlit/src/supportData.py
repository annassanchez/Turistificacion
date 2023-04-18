import pandas as pd
import requests
import xmltodict
import json
import pickle
import fiona
import geopandas as gpd
pd.set_option('display.max_columns', None)
from IPython.display import clear_output

def extractHotels():
    """
    this function extracts the information for hotels from the Ayuntamiento de Madrid, transforms the output from the API and returns a dataframe with the desired columns.
    - Retrieve the hotel information in XML format from the given URL using requests.get() method.
    - Convert the obtained XML data into a dictionary and extract the required information needed for each hotel from the dictionaries on basicData, geoData, and extradata.
    - Further extract the information for categories cat1_num, cod1_txt, cat2_num, cod2_txt, cat3_num, and cod3_txt from the sub-dictionaries of 'categorias' in the original data
    """
    ## getting the datatrame from the api
    print('calling API')
    url_hotels = 'https://www.esmadrid.com/opendata/alojamientos_v1_es.xml'
    res_hotels = requests.get(url_hotels)
    df_hotels = pd.DataFrame(xmltodict.parse(res_hotels.text)['serviceList']['service'])
    ## extracting the info from dictionaries on `basicData`, `geoData`, `extradata`
    print('cleaning data')
    df_hotels = pd.concat([df_hotels, df_hotels['basicData'].apply(pd.Series), df_hotels['geoData'].apply(pd.Series), df_hotels['extradata'].apply(pd.Series)], axis = 1)
    item = df_hotels['item'].apply(pd.Series)#['categoria'].apply(pd.Series)
    ## getting `cat1_num`, `cod1_txt``
    cat1_num = item[0].apply(pd.Series).rename({'#text':'cod1_num'}, axis = 1).drop(['@name'], axis = 1)
    cod1_txt = item[1].apply(pd.Series).rename({'#text':'cod1_txt'}, axis = 1).drop(['@name'], axis = 1)
    ## getting `cat2_num`, `cod2_txt``
    categoria = df_hotels['categorias'].apply(pd.Series)['categoria'].apply(pd.Series)
    item = categoria['item'].apply(pd.Series)#[0].apply(pd.Series)
    cat2_num = item[0].apply(pd.Series).rename({'#text':'cod2_num'}, axis = 1).drop(['@name', 0], axis = 1)
    cod2_txt = item[1].apply(pd.Series).rename({'#text':'cod2_txt'}, axis = 1).drop(['@name', 0], axis = 1)
    ## getting `cat3_num`, `cod3_txt``
    estrellas = categoria['subcategorias'].apply(pd.Series)['subcategoria'].apply(pd.Series)['item'].apply(pd.Series)#[1].apply(pd.Series)
    cat3_num = estrellas[0].apply(pd.Series).rename({'#text':'cod3_num'}, axis = 1).drop(['@name', 0], axis = 1)
    cod3_txt = estrellas[1].apply(pd.Series).rename({'#text':'cod3_txt'}, axis = 1).drop(['@name', 0], axis = 1)
    ## nerging all slices
    df_hotels = pd.concat([df_hotels, cat1_num, cod1_txt, cat2_num, cod2_txt, cat3_num, cod3_txt], axis = 1)
    df_hotels.drop(['basicData', 'geoData', 'multimedia', 'extradata', 'item', 'categorias'], axis = 1, inplace = True)
    print('saving the output')
    with open(f'../data/ayto_madrid/ayto_madrid_hotels.pickle', 'wb') as f:
        pickle.dump(df_hotels, f)
    return df_hotels

def censoLocalesTerrazas(year, month):
    """
    this function gathers info on business activites (shops, bars,...), census of business premises, bar terraces and the historic census of premises.
    It contacts the Ayuntamiento de Madrid API and gathers the last info available, transforms the data and returns separated dataframes for the given info.
    Once the API returns the data, it returns a json and it can be transformed to a dataframe.
    args: year -> the year the data was last published
        month -> the month the data was las publisehd
    output: df_actividades -> returns a dataframe with the current business activites
        df_local -> returns a dataframe with the census of business premises
        df_terrazas -> returns a dataframe with the bar terraces
        df_licencia -> returns a dataframe with the historic census of premises
    """
    # actividades
    print('calling API')
    url_actividades = f'https://datos.madrid.es/datosabiertos/CIUAB/CENSO/ACTIVIDADECONOMICA/{year}/{month}/actividadeconomica{year}{month}.json'
    res_actividades = requests.get(url_actividades)
    df_actividades = pd.DataFrame(res_actividades.json())
    # lcoal
    url_local = f'https://datos.madrid.es/datosabiertos/CIUAB/CENSO/LOCALES/{year}/{month}/locales{year}{month}.json'
    res_local = requests.get(url_local)
    df_local = pd.DataFrame(res_local.json())
    # terrazas
    url_terrazas = f'https://datos.madrid.es/datosabiertos/CIUAB/CENSO/TERRAZAS/{year}/{month}/terrazas{year}{month}.json'
    res_terrazas = requests.get(url_terrazas)
    df_terrazas = pd.DataFrame(res_terrazas.json())
    # licencias
    url_licencia = 'https://datos.madrid.es/egob/catalogo/200085-29-censo-locales.json'
    res_licencia = requests.get(url_licencia)
    df_licencia = pd.DataFrame(res_licencia.json())
    for filename, file in zip(['df_actividades', 'df_local', 'df_terrazas', 'df_licencia'], [df_actividades, df_local, df_terrazas, df_licencia]):
        print(f'saving the output for {filename}')
        with open(f'../data/ayto_madrid/ayto_madrid_{filename}.pickle', 'wb') as f:
            pickle.dump(file, f)
    return df_actividades, df_local, df_terrazas, df_licencia

def catastroLayers(path):
    """
    Function description:
    This function takes a file path of a geopackage as input and returns a dictionary containing GeoDataFrames for each layer present in the geopackage. 
    It first uses fiona.listlayers to get a list of layer names in the geopackage and prints that list to the console. 
    It then initializes an empty dictionary and iterates through the list of layer names obtained from fiona.listlayers. 
    For each layer, it reads the layer data into a GeoDataFrame using gpd.read_file and adds that GeoDataFrame to the output dictionary using a unique integer key. 
    Finally, it returns the output dictionary containing GeoDataFrames for all layers in the input geopackage.
    Input parameter:
        - path: a string representing the file path of a geopackage
    Output:
        - A dictionary where keys are integers and values are GeoDataFrames, each corresponding to a layer in the input geopackage.
    """
    layers = fiona.listlayers(path)
    print(f'the geopackage has layers: {layers}')
    gdf_dict = {}
    for i, layer in enumerate(layers):
        print(f'adding layer {layer} to the output dictionary...')
        gdf_dict[i] = gpd.read_file(path, layer = layer)
        print(f'done')
    return gdf_dict

def importDatasets():
    df_2017 = gpd.read_file('../output/grid_2017.geojson').to_crs(epsg=4326)

    neighborhoods = gpd.read_file('../data/airbnb_airdna/2022_06_07/neighbourhoods.geojson').to_crs(epsg=4326)

    df_2023 = gpd.read_file('../output/grid_2023.geojson').to_crs(epsg=4326)

    gdf_2023 = neighborhoods.sjoin(df_2023, how="left")

    gdf_2017 = neighborhoods.sjoin(df_2017, how="left")

    return gdf_2017, gdf_2023