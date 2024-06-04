import streamlit as st

st.write("Hello,This is my first web app for a ML model")
st.title ("Customer Churn Predictor")
st.subheader("Page 4 : Predictor using the ML models created")
x=st.text_input('Senior Citizen?')
st.write (f'Your movie is : {x}')
x=st.text_input('Relationship Status?')
st.write (f'Your movie is : {x}')
x=st.text_input('Dependents?')
st.write (f'Your movie is : {x}')
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')