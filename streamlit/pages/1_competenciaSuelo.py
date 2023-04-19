import seaborn as sns
import pandas as pd
import matplotlib.pyplot as  plt
import streamlit as st
import plotly.express as px
import numpy as np
import sys
#sys.path.append("../")
import src.supportImages as si
#sys.path.append("../")
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
    # Check if selected option is a valid column name
    #if options and options[0] in gdf_2023_competencia.columns:
    #    fig = px.choropleth(data_frame=df_2023_competencia, color=options[0],
    #                        geojson=gdf_2023_competencia['geometry'],
    #                        locations="neighbourhood",
    #                        featureidkey="properties.neighbourhood",
    #                        center=dict(lat=40.0, lon=-3.72),
    #                        labels={options[0]: options[0]}
    #                        )
    #else:
    #    st.plotly_chart(fig)
    #    st.write('Please select a valid option.')
    st.markdown('2023')
    if options and options[0] in gdf_2023_competencia.columns:
        si.plotMap2023(gdf_2023_competencia, options[0])
        #st.image(f'images/testMap_{options[0]}_2023.png')
        st.image(f'images/mapTest_{options[0]}_2023.png')
    else:
        st.write('Please select a valid option.')

with col2:
    # Check if selected option is a valid column name
    #if options and options[0] in gdf_2023_competencia.columns:
    #    fig = px.choropleth(data_frame=df_2023_competencia, color=options[0],
    #                        geojson=gdf_2023_competencia['geometry'],
    #                        locations="neighbourhood",
    #                        featureidkey="properties.neighbourhood",
    #                        center=dict(lat=40.0, lon=-3.72),
    #                        labels={options[0]: options[0]}
    #                        )
    #else:
    #    st.plotly_chart(fig)
    #    st.write('Please select a valid option.')
    st.markdown('2017')
    if options and options[0] in gdf_2017_competencia.columns:
        si.plotMap2017(gdf_2017_competencia, options[0])
        #st.image(f'images/testMap_{options[0]}_2017.png')
        st.image(f'images/mapTest_{options[0]}_2017.png')
    else:
        st.write('Please select a valid option.')

with col3:
    df = sd.differenceGrids(df_2017_competencia, df_2023_competencia)
    neighbourhood = st.multiselect(
        'Choose a neighbourhood to observe',
        df['neighbourhood'].tolist(),
        ['Sol'])
    if options and options[0] in gdf_2017_competencia.columns:
        #st.metric(label=df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'].iat[0],
        #        value=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'{options[0]}_2023'].iat[0], 2),
        #        delta=np.round(df.loc[df['neighbourhood'] == neighbourhood[0], f'{options[0]}_2017_ratio'].iat[0]*100, 2))
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
    #st.markdown(f'{options[0]}_2023')
    #st.dataframe(df.loc[df['neighbourhood'] == neighbourhood[0], 'neighbourhood'])
    #st.dataframe(df.loc[df['neighbourhood'] == neighbourhood[0], f'{options[0]}_2023'])
    #fig.update_geos(fitbounds="locations", visible=False)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#st.plotly_chart(fig)