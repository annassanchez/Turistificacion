import streamlit as st
import streamlit.components.v1 as components
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import json
import pickle

#with open(f'../streamlit/html/kepler.gl.html', 'r') as f:
#            html = f.read()

#html_file = open("../streamlit/html/kepler.gl(1).html", 'r')

#st.markdown(html_file)


#plot_file = open('plot.html','r')

#plot = html_file.read()

#components.html(
#    html=plot
#)

#plot = html_file.close()


with open(f'config/alcohol_airbnb_offer_2023.pickle', 'rb') as configuration:
            config2 = pickle.load(configuration)
with open(f'../output/maps/grid_2023.geojson', 'r') as f:
    geojson2 = f.read()
map_1 = KeplerGl(height=400, data=geojson2,config=config2)
keplergl_static(map_1)