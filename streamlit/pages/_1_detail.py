import streamlit as st
import streamlit.components.v1 as components

with open(f'../streamlit/html/kepler.gl.html', 'r') as f:
            html = f.read()

html_file = open("../streamlit/html/kepler.gl(1).html", 'r')

#st.markdown(html_file)


#plot_file = open('plot.html','r')

plot = html_file.read()

components.html(
    html=plot
)

plot = html_file.close()