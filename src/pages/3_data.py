import streamlit as st
import pandas as pd
import matplotlib as plt


st.title ("Data of Customers")
st.subheader("This is a breakdown of customer attrition attributes")
x=st.text_input('Fovourite Movie?')
st.write (f'Your movie is : {x}')
