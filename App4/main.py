import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use("ggplot")
data = {
    'num': [x for x in range(1,11)],
    'square':[x for x in range(1,11)],
    'twice': [x for x in range(1,11)],
    'thrice': [x for x in range(1,11)]
}
df = pd.DataFrame(data= data)
#st.sidebar.selectbox("Select a Number:",[1,2,3,4,5])
#col = st.sidebar.selectbox('Select a Column',df.columns)
col = st.sidebar.multiselect('Select a Column',df.columns)
plt.plot(df['num'],df[col])
#fig, ax = plt.subplots()
#ax.scatter(data,data) 
st.pyplot()