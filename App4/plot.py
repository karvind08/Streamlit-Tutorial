import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns= ['A','B','C']
)

# Line Chart 
st.subheader('Line Chart')
st.line_chart(data)

# Area Chart 
st.subheader('Area Chart')
st.area_chart(data)

# Bar Chart 
st.subheader('Bar Chart')
st.bar_chart(data)

# # Matplotlib
# plt.scatter(data['A'],data['B'])
# plt.title("Scatter Plot using Matplotlib")
# st.pyplot()

# Altair
st.subheader('Altair ')
chart = alt.Chart(data).mark_circle().encode(
    x = 'A', y = 'B',tooltip= ['A','B']
)
st.graphviz_chart("""
diagraph {
    watch -> like
    like ->share
    share -> subscribe
    share -> watch                  
}
""")
st.altair_chart(chart,use_container_width=True)

st.subheader("Map")

city = pd.DataFrame(
{
    'mycity': ['Delhi','Chennai','Kolkata'],
    'lat': [28.679079,13.067439,22.572645],
    'lon': [77.069710,80.237617,88.363892],
})
st.map(city)

# Image
st.subheader("Image")
st.image("logo.png",width=200)

st.subheader("Audio")
st.audio("https://soundcloud.com/audio-files/sets/new-yorkers-make-their-voices?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")

st.subheader("Video")
st.video("https://youtu.be/-uCYHPV-kRc")