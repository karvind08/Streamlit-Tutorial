import streamlit as st
st.title("Session States")
st.header("Counter")
count = 0
if increment := st.button("Add 1"):
    count = count + 1
st.write(count)