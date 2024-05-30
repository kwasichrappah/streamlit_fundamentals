import streamlit as st

st.write("Hello,This is my first web app for a ML model")
st.title ("Customer Churn Predictor")
st.caption("storage of all the predicted outcomes")
x=st.text_input('Fovourite Movie?')
st.write (f'Your movie is : {x}')
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')