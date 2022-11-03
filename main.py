import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

option2 = st.selectbox(
    'Which number is a multiple of 10 ;)',
    df['second column'])

'You selected: ', option
'you selected', option2

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

if st.checkbox('show table'):
    chart_data = pd.DataFrame({
        'Name' : ['Anujan', 'Reuben'],
        'Age' : [17,17]
    })
    st.write(chart_data)
        
    


st.write("Hello World!*")
st.write(st.slider("what"))



st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
