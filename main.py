"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import mymodel as m

st.write("Hello World!*")
st.write(m.run(window=15))
