import streamlit as st

st.write("Hello,This is my first web app for a ML model")
st.title ("Customer Churn Predictor")
st.subheader("Page 3 : Predictor using the ML models created")
x=st.text_input('Fovourite Movie?')
st.write (f'Your movie is : {x}')
