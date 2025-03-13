import streamlit as st
st.title("About us")

col1,col2 = st.columns(2,gap="small",vertical_alignment="center")

with col1:
    st.image("./assets/logo.png", width=150)


with col2:
    st.title("Arvind", anchor=False)
    st.write("Founder, Actolaze Technology LLP, Kharwal Academy - The School of Programming")
