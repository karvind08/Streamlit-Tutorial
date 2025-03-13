import streamlit as st
from streamlit_option_menu import option_menu

# with st.sidebar:
#     selected = option_menu(
#         menu_title="Main Menu",
#         menu_icon=":material/account-circle:",
#         options = ["Home","About","Contact"]
#     )

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options = ["Home","About","Contact"],
        menu_icon=":material/account-circle:",
        icons  = ['house','book','person-rolodex'],
        default_index= 0,       
    )


selected = option_menu(
        menu_title=None,
        options = ["Home","About","Contact"],
        menu_icon=":material/account-circle:",
        icons  = ['house','book','person-rolodex'],
        default_index= 0,    
        orientation= "horizontal",
    )

if selected == "Home":
    st.title(f"You have selected {selected}")

if selected == "About":
    st.title(f"You have selected {selected}")

if selected == "Contact":
    st.title(f"You have selected {selected}")