# Adding widgets to streamlit app
import streamlit as st
st.title("Widgets")

st.subheader("Buttons")
st.button("I am Button")
if st.button("Subscribe"):
    st.write("Please subscribe")

st.subheader("Text Input")
st.text_input("First Name")

name = st.text_input("Name")
st.write(name)

st.subheader("Text Area")
address = st.text_area("Enter the address")
st.write(address)

