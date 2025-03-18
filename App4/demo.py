import streamlit as st
import pandas as pd
import numpy as np
# Data 
a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dict = {
    'Name': ['Jiya','Duggu'],
    'Age': ['Three','Four'],
    'Gender':['Female','Male'],
}
# Table in streamlit

st.table(dict)
st.markdown(''' *** ''')
# Json File
st.json(dict)