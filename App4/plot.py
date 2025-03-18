import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(100,3),
    columns= ['A','B','C']
)

# Line chart 
st.subheader('Line Chart')
st.line_chart(data)