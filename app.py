import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is a simple web app built with Streamlit.')


name = st.text_input("Enter your name:")
if st.button('Submit'):
    st.write(f"Hello, {name}!")
    
    
import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(data)


df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [24, 23, 34, 29]
})
st.write(df)

