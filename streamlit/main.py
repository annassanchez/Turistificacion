import streamlit as st
import pandas as pd
import numpy as np
import pickle
import geopandas as gpd
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import src.supportData as sd

st.set_page_config(layout="centered", initial_sidebar_state="collapsed", page_title='touristification', page_icon="")


gdf_2017_competencia, gdf_2023_competencia = sd.importCompetenciaDelSuelo()

st.title('Touristification')

st.markdown("""
    Touristification is a project that aims to create an atlas to measure the impact of tourism in the city of Madrid. 
    <br>This project is based on the research developed by the architecture studio [300.000 Km/s](http://turistificacion.300000kms.net/) based on multiple data sources: open statistical data (Catastro, Ayuntamiento de Madrid Open Data Platform) and soft-data (scraped or crawled from Tripadvisor and Airbnb).  
    Their analysis was based on data gathered around 2017, so the aim is to see if something has changed in the city of Madrid. AirBnB listings are growing? The residential house market has been affected? 
""", unsafe_allow_html = True)
