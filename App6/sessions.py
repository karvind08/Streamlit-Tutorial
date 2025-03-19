import streamlit as st
st.title("Session States")
st.header("Counter")

def add_one():
    st.session_state.counter +=1

if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

count = st.session_state.counter 
 
st.button('Add One',on_click=add_one)

# if increment := st.button("Add 1"):
#     count = count + 1
#     st.session_state.counter = count
st.write(count)