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

st.subheader("Slider")
st.slider("Age")
st.slider("Pointer",min_value=3,max_value=70)
st.slider("Marks",min_value=3,max_value=70,value=30)
st.slider("Step",min_value=3,max_value=70,value=33,step=2)
ss = st.slider("Point",min_value=3,max_value=70)
st.write(f" The value is {ss}")


st.subheader("Number Input")
st.number_input("Enter the number")
st.number_input("Number",min_value=3,max_value=70,value=33,step=2)
st.number_input("Number",min_value=3.0,max_value=70.0,value=23.0,step=2.0)

st.subheader("File Uploader")
st.file_uploader("Upload the file")
f = st.file_uploader("Image")
st.image(f)