import pandas as pd
import streamlit as st
import numpy as np
import sys
import pickle
#sys.path.append("../")
import src.supportImages as si
#sys.path.append("../")
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import src.supportData as sd

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title='comparison', page_icon="🔮")

gdf_2017_competencia, gdf_2023_competencia = sd.importCompetenciaDelSuelo()
df_2017_competencia = pd.DataFrame(gdf_2017_competencia.drop(columns='geometry'))
df_2023_competencia = pd.DataFrame(gdf_2023_competencia.drop(columns='geometry'))

options = st.multiselect(
    'Choose a variable to observe',
    gdf_2023_competencia.columns.tolist()[1:-2],
    [])

#sch.plotMap(gdf_2017, options)
col1, col2, col3= st.columns(3)

with col1:
    st.markdown('2023')
    if options and options[0] in gdf_2023_competencia.columns:
        year2 = 2023
        variable2 = options[0] + '_' + str(year2)
        with open(f'config/{variable2}.pickle', 'rb') as configuration:
            config2 = pickle.load(configuration)
        with open(f'../output/maps/grid_competencia_suelo_{year2}.geojson', 'r') as f:
            geojson2 = f.read()
        map_2 = KeplerGl(height=400, data={variable2: geojson2},config=config2)
        keplergl_static(map_2)
    else:
        st.write('Please select a valid option.')

with col2:
    st.markdown('2017')
    if options and options[0] in gdf_2017_competencia.columns:
        year1 = 2017
        variable1 = options[0] + '_' + str(year1)
        with open(f'config/{variable1}.pickle', 'rb') as configuration:
            config1 = pickle.load(configuration)
        with open(f'../output/maps/grid_competencia_suelo_{year1}.geojson', 'r') as f:
            geojson1 = f.read()
        map_1 = KeplerGl(height=400, data={variable1: geojson1},config=config1)
        keplergl_static(map_1)
    else:
        st.write('Please select a valid option.')

with col3:
    df = sd.differenceGrids(df_2017_competencia, df_2023_competencia)
    neighbourhood = st.multiselect(
        'Choose a neighbourhood to observe',
        df['neighbourhood'].tolist(),
        ['Sol'])
    if options and options[0] in gdf_2017_competencia.columns:
        col1, col2, col3, col4= st.columns(4)
        with col1:
            st.markdown('fotocasa listings')
            st.metric(label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'fc_tot_offer_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'fc_tot_offer_2017_ratio'].iat[0], 2))
        with col2:
            st.markdown('airbnb listings')
            st.metric(label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'abnb_tot_offer_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'abnb_tot_offer_2017_ratio'].iat[0], 2))    
        with col3:
            st.markdown('airbnb total price')
            st.metric(label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'abnb_tot_price_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'abnb_tot_price_2017_ratio'].iat[0], 2))
        with col4:
            st.markdown('residential vs p2p listings')
            st.metric(label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'resi_vs_p2p_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'resi_vs_p2p_2017_ratio'].iat[0], 2))
        st.dataframe(df.loc[df['neighbourhood'] == neighbourhood[0], ['neighbourhood', f'{options[0]}_2023', f'{options[0]}_2017', f'{options[0]}_2017_ratio']], height=100)
    else:
        st.write('Please select a valid option.')