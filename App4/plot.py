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
    x = 'A',
    y = 'B'
)
st.altair_chart(chart)
