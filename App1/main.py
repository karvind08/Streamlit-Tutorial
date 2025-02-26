import streamlit as st
st.title("My First Streamlit app")
st.text("This is text\n[and more text](that's not a Markdown link).")
st.text("This is another text",help='This is streamlit text')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")