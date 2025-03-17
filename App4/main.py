import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import time
plt.style.use("ggplot")
data = {
    'num': [x for x in range(1,11)],
    'square':[x for x in range(1,11)],
    'twice': [x for x in range(1,11)],
    'thrice': [x for x in range(1,11)]
}
df = pd.DataFrame(data= data)
rad = st.sidebar.radio("Navigantion",["Home","About us"])
if rad == "Home":
    #st.sidebar.selectbox("Select a Number:",[1,2,3,4,5])
    col = st.sidebar.selectbox('Select a Column',df.columns)
    # col = st.sidebar.multiselect('Select a Column',df.columns)
    plt.plot(df['num'],df[col])
    # #fig, ax = plt.subplots()
    # #ax.scatter(data,data) 
    st.pyplot()
if rad == "About us":
    st.write("You are at About us Page")
    st.error("Error")
    st.success("Success")
    st.info("Information")
    st.exception(RuntimeError("Run Time Error or Exception"))
    st.warning("Warning")
    st.subheader("Progress Bar")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
