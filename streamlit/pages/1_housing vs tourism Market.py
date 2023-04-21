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
import src.biblio as bb

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title='comparison', page_icon="🔮")

gdf_2017, gdf_2023 = sd.importFiesta()
df_2017_competencia = pd.DataFrame(gdf_2017.drop(columns='geometry'))
df_2023_competencia = pd.DataFrame(gdf_2023.drop(columns='geometry'))

options = st.multiselect(
    'Choose a variable to observe',
    gdf_2023.columns.tolist()[1:-3],
    ['abnb_tot_offer'])

#options = options_matched.replace(bb.fiesta)

#sch.plotMap(gdf_2017, options)
col1, col2, col3= st.columns(3)

with col1:
    st.markdown('2017')
    if options and options[0] in gdf_2017.columns:
        year1 = 2017
        variable1 = options[0] + '_' + str(year1)
        with open(f'config/{variable1}.pickle', 'rb') as configuration:
            config1 = pickle.load(configuration)
        with open(f'../output/maps/grid_fiesta_{year1}.geojson', 'r') as f:
            geojson1 = f.read()
        map_1 = KeplerGl(height=400, data={variable1: geojson1},config=config1)
        keplergl_static(map_1)
    else:
        st.write('Please select a valid option.')
    
with col2:
    st.markdown('2023')
    if options and options[0] in gdf_2023.columns:
        year2 = 2023
        variable2 = options[0] + '_' + str(year2)
        with open(f'config/{variable2}.pickle', 'rb') as configuration:
            config2 = pickle.load(configuration)
        with open(f'../output/maps/grid_fiesta_{year2}.geojson', 'r') as f:
            geojson2 = f.read()
        map_2 = KeplerGl(height=400, data={variable2: geojson2},config=config2)
        keplergl_static(map_2)
    else:
        st.write('Please select a valid option.')

with col3:
    df = sd.differenceGrids(df_2017_competencia, df_2023_competencia)
    neighbourhood = st.multiselect(
        'Choose a neighbourhood to observe',
        df['neighbourhood'].tolist(),
        ['Sol'])
    if options and options[0] in gdf_2023.columns:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('AirBnB # offers')
            st.metric(#label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                label='',
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'abnb_tot_offer_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'abnb_tot_offer_2017_ratio'].iat[0], 2))
        with col2:
            st.markdown('AirBnB stock')
            st.metric(#label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                label='',
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'stock_airbnb_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'stock_airbnb_2017_ratio'].iat[0], 2))    
        with col3:
            st.markdown('AirBnB avg price €')
            st.metric(#label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                label='',
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'abnb_tot_price_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'abnb_tot_price_2017_ratio'].iat[0], 2))
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown('Number of sex shops', unsafe_allow_html = True)
            st.metric(#label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                label='',
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'local200_n_sex_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'local200_n_sex_2017_ratio'].iat[0], 2))
            
        with col2:
            st.markdown('Number licquor stores', unsafe_allow_html = True)
            st.metric(#label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                label ='',
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'local200_n_prox_alcohol_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'local200_n_prox_alcohol_2017_ratio'].iat[0], 2))   
        with col3:
            st.markdown('Number restaurants', unsafe_allow_html = True)
            st.metric(#label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                label='',
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'local200_n_restaurants_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'local200_n_restaurants_2017_ratio'].iat[0], 2))
        with col4:
            st.markdown('Number nightclubs', unsafe_allow_html = True)
            st.metric(#label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
                label='',
                value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'local200_n_fiesta_2023'].iat[0], 2),
                delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'local200_n_fiesta_2017_ratio'].iat[0], 2)) 
       #st.dataframe(df.loc[df['neighbourhood'] == neighbourhood[0], ['neighbourhood', f'{options[0]}_2023', f'{options[0]}_2017', f'{options[0]}_2017_ratio']], height=100)
    else:
        st.write('Please select a valid option.')