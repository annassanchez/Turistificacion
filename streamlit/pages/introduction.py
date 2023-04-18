import seaborn as sns
import matplotlib.pyplot as  plt
import streamlit as st
import plotly.express as px
import sys
sys.path.append("../")
import src.supportCharts as sch
sys.path.append("../")
import src.supportData as sd

options = st.multiselect(
    'Choose a variable to observe',
    ['restaurants', 'prox_fresco'],
    [])

gdf_2017, gdf_2023 = sd.importDatasets()

#sch.plotMap(gdf_2017, options)

# Check if selected option is a valid column name
if options and options[0] in gdf_2023.columns:
    fig = px.choropleth(gdf_2023, color=options[0],
                        geojson=gdf_2023['geometry'],
                        locations="neighbourhood", 
                        featureidkey="properties.geometry",
                        projection="mercator",
                        labels={
                            f'{options}':f'{options}'
                            }
                       )

    st.plotly_chart(fig)
else:
    st.write('Please select a valid option.')
#fig.update_geos(fitbounds="locations", visible=False)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#st.plotly_chart(fig)