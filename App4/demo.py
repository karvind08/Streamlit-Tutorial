import streamlit as st
import pandas as pd
import numpy as np

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dict = {
    'Name': ['Jiya','Duggu'],
    'Age': ['Three','Four'],
    'Gender':['Female','Male'],
}
st.table(dict)
