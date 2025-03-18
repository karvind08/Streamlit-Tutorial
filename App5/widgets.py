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

st.subheader("Date")
dt = st.date_input("Enter the date")
st.write(f"The date is {dt}")

st.subheader("Time")
tt = st.time_input("Enter time")
st.write(f"The current time {tt}")

st.subheader("Checkbox")
st.checkbox("You accept Terms & condition",value=False)
st.checkbox(" Another Terms & condition",value=True)

if st.checkbox("Terms & condition",value=False):
    st.write("Thank you")

st.subheader("Radio")
st.radio("Programming",['C','C++','Python'],index=0)
pgs = ['C','C++','Python','Java']
r1 = st.radio("Programming",pgs,index=0)


st.subheader("Selectbox")
pgs = ['C','C++','Python','Java']
s1 = st.selectbox("Programming",pgs,index=2)
st.write(r1,s1)

st.subheader("Multi Select")
st.multiselect("Programmings",pgs)

ms = st.multiselect("Program",pgs)
st.write(ms)

