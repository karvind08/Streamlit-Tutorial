import streamlit as st
import pandas as pd
import numpy as np
import time
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

st.markdown(''' *** ''')

# CSV File

data = pd.read_csv('award.csv')
st.write(data)

st.write(a)

st.write(dict)

st.write(nd)

# Caching Mechanism in Streamlit

# @st.cache
# def ret_time():
#     time.sleep(5)
#     return time.time()