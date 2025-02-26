import streamlit as st
st.title("My First Streamlit app")
st.text("This is text\n[and more text](that's not a Markdown link).\n")
st.text("\nThis is another text",help='This is streamlit text')

code = '''def hello():
    print("Hello, Streamlit!")
    print('I am Arvind')'''
st.code(code, language="python",line_numbers=True,wrap_lines=True, height=80)
code1 = '''Is it a crown or boat?
                        ii
                      iiiiii
WWw                 .iiiiiiii.                ...:
 WWWWWWw          .iiiiiiiiiiii.         ........
  WWWWWWWWWWw    iiiiiiiiiiiiiiii    ...........
   WWWWWWWWWWWWWWwiiiiiiiiiiiiiiiii............
    WWWWWWWWWWWWWWWWWWwiiiiiiiiiiiiii.........
     WWWWWWWWWWWWWWWWWWWWWWwiiiiiiiiii.......
      WWWWWWWWWWWWWWWWWWWWWWWWWWwiiiiiii....
       WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWwiiii.
          -MMMWWWWWWWWWWWWWWWWWWWWWWMMM-
'''
st.code(code1, language=None)