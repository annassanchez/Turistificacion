import streamlit as st
import pandas as pd
import numpy as np
import pickle
import geopandas as gpd
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import src.supportData as sd

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title='touristification', page_icon="")


gdf_2017_competencia, gdf_2023_competencia = sd.importCompetenciaDelSuelo()



col1, col2, col3 = st.columns([1,3,1])
with col1:
    st.markdown('')
with col2:
    st.title('Touristification')

    st.markdown("""
        Touristification is a project that aims to create an atlas to measure the impact of tourism in the city of Madrid. 
        <br>This project is based on the research developed by the architecture studio [300.000 Km/s](http://turistificacion.300000kms.net/) based on multiple data sources: open statistical data (Catastro, Ayuntamiento de Madrid Open Data Platform) and soft-data (scraped or crawled from Tripadvisor and Airbnb).  
        Their analysis was based on data gathered around 2017, so the aim is to see if something has changed in the city of Madrid. AirBnB listings are growing? The residential house market has been affected? 
    """, unsafe_allow_html = True)

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric(
            label='cadaster buildings data',
            value=gpd.read_file('../output/geojson/catastro.geojson').shape[0]
        )
    with col2:
        st.metric(
            label='airbnb listings data',
            value=gpd.read_file('../output/geojson/airbnb.geojson').shape[0]
        )
    with col3:
        st.metric(
            label='fotocasa listings data',
            value=gpd.read_file('../output/geojson/fotocasa.geojson').shape[0]
        )
    with col4:
        st.metric(
            label='hotels licenses data',
            value=gpd.read_file('../output/geojson/hotels.geojson').shape[0]
        )
    with col5:
        st.metric(
            label='busines premises data',
            value=gpd.read_file('../output/geojson/locales.geojson').shape[0]
        )
    with col6:
        st.metric(
            label='tripadvisor restaurants data',
            value=gpd.read_file('../output/geojson/tripadvisor.geojson').shape[0]
        )
with col1:
    st.markdown('')