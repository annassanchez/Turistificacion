import numpy as np
import pandas as pd
import pickle
import math
import geopandas as gpd

#display
from IPython.display import display
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as ticker
import seaborn as sns
plt.rcParams["figure.figsize"] = (10,8)
from IPython.display import clear_output
import folium
import contextily as cx

import warnings
warnings.filterwarnings('ignore')

def analisis_basico(dataframe):
    """
    esta función coge un dataframe y saca los principales elementos preiminares de un eda: la estructura de datos, si hay nulos, duplicados, el tipo de variables numéricas o categórcias y un pairplot para ver la relación entre variables.
    param: dataframe
    """
    print("_________________________________\n")
    print (f"1_Data Structure: {dataframe.shape}")
    display(dataframe.head(2))
    display(dataframe.info())
    print("_________________________________\n")
    print("2_Duplicated columns:") 
    print(dataframe.duplicated().sum())
    print("_________________________________\n")
    print("3_Null values distribution:")
    display(pd.concat([dataframe.isnull().sum(), dataframe.dtypes], axis = 1).rename(columns = {0: "nulos", 1: "dtypes"}).T)
    print("_________________________________\n")
    print("4_Numerical variables distribution:")
    display(dataframe.describe())
    print("_________________________________\n")
    print("5_Categorical variables distribution:")
    try:
        display(dataframe.describe(include = "object"))
    except:
        print("No categorical variables available, sorry :(") 
        pass

def regplot_numericas(dataframe, columnas_drop, variable_respuesta):
    """
    esta función da un chart que relaciona las columnas numéricas de un dataframe con la variable
    param: dataframe -> el dataframe a representar
        columnas_drop -> las columnas a borrar (un id alguna columna que no se quiera representar) -> se pasa en formato lista
        variable_respuesta -> las columnas a borrar (en este caso, la variable respuesta)
    """
    print(f'distribución de las variables numéricas en relación con la variable respuesta: {variable_respuesta}')
    df_numericas = dataframe.select_dtypes(include = np.number)
    columnas = df_numericas.drop(columnas_drop, axis = 1)
    fig, axes = plt.subplots(nrows=int(columnas.shape[1]/2), ncols=int(columnas.shape[1] / 3), figsize = (10 * columnas.shape[1] / 2,10 * columnas.shape[1] / 3))
    axes = axes.flat
    for i, columns in enumerate(columnas.columns):
        sns.regplot(data = dataframe, 
            x = columns, 
            y = variable_respuesta, 
            ax = axes[i],
            color = 'gray',
            scatter_kws = {"alpha": 0.4}, 
            line_kws = {"color": "red", "alpha": 0.7 }
            )
    fig.tight_layout();

def chart_categoricas_count(df):
    """
    esta función toma un dataframe y presnta unos histogramas con las variables categóricas
    param: dataframe -> dataframe del que se sacan los gráficos
    """
    print(f'this chart gives the categorical distribution of the variables')
    df_cat = df.select_dtypes(include = np.number)
    fig, axes = plt.subplots(nrows=int(df_cat.shape[1]/2), ncols=int(df_cat.shape[1] / 3), figsize = (10 * df_cat.shape[1] / 2,10 * df_cat.shape[1] / 3))
    axes = axes.flat

    for i, colum in enumerate(df_cat.columns):
        chart = sns.countplot(
                x = df_cat[colum],
                #hue = df_cat['Offer_Accepted'],
                ax = axes[i])
        total = float(len(df_cat[colum]))
        for p in chart.patches:
            height = p.get_height()
            chart.text(p.get_x() + p.get_width() / 2., height + 3,
                    '{:.2f}%'.format((height / total) * 100),
                    ha='center')
    fig.tight_layout();

def chart_boxplot(dataframe):
    """
    esta funcion saca los boxplots de las variables numéricas - incluyendo la variable respuesta
    param: dataframe
    """
    print('numeric variables distribution -> outliers')
    dataframe = dataframe.select_dtypes(include = np.number)
    fig, ax = plt.subplots(dataframe.shape[1], 1, figsize=(25, 2.5 * dataframe.shape[1]))

    for i in range(len(dataframe.columns)):
        sns.boxplot(x=dataframe.columns[i], data=dataframe, ax=ax[i])
        ax[i].tick_params(labelsize=10)
    plt.tight_layout()
    plt.show();

def distribucion_numericas(dataframe):
    """
    Genera un conjunto de gráficos de distribución (KDE) para las variables numéricas de un dataframe.
    Args:
        dataframe (pandas.DataFrame): El dataframe que se desea analizar.
    Returns:
        None: La función no retorna ningún valor.
    """
    print('numeric variables distribution')
    # Obtener las columnas numéricas del dataframe
    columnas_numeric = dataframe.select_dtypes(include=np.number).columns

    # Crear el conjunto de subplots para graficar las distribuciones
    fig, axes = plt.subplots(nrows=int(np.ceil(len(columnas_numeric)/2)), ncols=2, figsize=(25, 15))
    axes = axes.flat

    # Graficar la distribución de cada variable
    for i, colum in enumerate(columnas_numeric):
        sns.histplot(
            data=dataframe,
            x=colum,
            alpha=0.2,
            kde=True,
            ax=axes[i])

        axes[i].set_title(colum, fontsize=15, fontweight="bold")
        axes[i].tick_params(labelsize=10)
        axes[i].set_xlabel("")

    fig.tight_layout()

def foliumMap(gdf, map_type):
    map1 = folium.Map(
            location=[40.41694, -3.70361],
            tiles='cartodbpositron',
            zoom_start=12,
        )
    if map_type == 'points':
        if gdf.shape[1] < 10000:
            gdf[gdf['longitude'].isnull() == False].apply(lambda row:folium.CircleMarker(location=[row["latitude"], row["longitude"]]).add_to(map1), axis=1)
            return map1
        else:
            gdf[gdf['longitude'].isnull() == False].apply(lambda row:folium.CircleMarker(location=[row["latitude"], row["longitude"]]).add_to(map1), axis=1)
            return map1
    elif map_type == 'polygon':
        for _, r in gdf.iterrows():
            sim_geo = gpd.GeoSeries(r['geometry'])
            geo_j = sim_geo.to_json()
            geo_j = folium.GeoJson(data=geo_j,
                                style_function=lambda x: {'fillColor': 'orange'})
            try:
                folium.Popup(r['name']).add_to(geo_j)
            except:
                pass
            geo_j.add_to(map1)
        return map1
    
def plotMap2023(gdf, column):
    if gdf.shape[1] < 10000:
        ax = gdf.to_crs(epsg=3857).plot(column=column, cmap=None)
        cx.add_basemap(ax)
        plt.tight_layout()
        plt.savefig(f'images/mapTest_{column}_2023.png');
    else:
        gdf = gdf.sample(10000)
        ax = gdf.to_crs(epsg=3857).plot(column=column, cmap=None)
        cx.add_basemap(ax)
        plt.tight_layout()
        plt.savefig(f'images/mapTest_{column}_2023.png');

def plotMap2017(gdf, column):
    if gdf.shape[1] < 10000:
        ax = gdf.to_crs(epsg=3857).plot(column=column, cmap=None)
        cx.add_basemap(ax)
        plt.tight_layout()
        plt.savefig(f'images/mapTest_{column}_2017.png');
    else:
        gdf = gdf.sample(10000)
        ax = gdf.to_crs(epsg=3857).plot(column=column, cmap=None)
        cx.add_basemap(ax)
        plt.tight_layout()
        plt.savefig(f'images/mapTest_{column}_2017.png');