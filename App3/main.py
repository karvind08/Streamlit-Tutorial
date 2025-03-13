import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        menu_icon=":material/account-circle:",
        options = ["Home","About","Contact"]
    )
if selected == "Home":
    st.title(f"You have selected {selected}")

if selected == "About":
    st.title(f"You have selected {selected}")

if selected == "Contact":
    st.title(f"You have selected {selected}")