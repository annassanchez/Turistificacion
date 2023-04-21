import streamlit as st
import streamlit.components.v1 as components
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import json
import pickle

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title='touristification', page_icon="")


#open kepler.gl(1).html file with streamlit components.html 
with open(f'../streamlit/html/alcohol_airbnb_offer_2023.html', 'r') as f:
    html = f.read()
components.html(html, height=600, width=1500)