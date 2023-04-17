import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
import branca
import geopandas as gpd

st.title('test')



# center on Liberty Bell, add mark
m2 = folium.Map(
        location=[40.41694, -3.70361],
        tiles='cartodbpositron',
        zoom_start=12,
    )

gdf = gpd.read_file('../data/airbnb_airdna/2023_03_13/neighbourhoods.geojson')

folium.GeoJson(gdf, style_function=lambda feature: {
    'color': 'black',
    'weight': 1,
    'dashArray': '5, 5',
    'fillOpacity':0.5
}).add_to(m2)

# call to render Folium map in Streamlit, but don't get any data back
# from the map (so that it won't rerun the app when the user interacts)
st_folium(m2, width=725, returned_objects=[])