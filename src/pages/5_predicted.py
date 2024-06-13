import streamlit as st
import pandas as pd
import joblib
import os
import datetime

st.set_page_config(
    page_title= "Predict Page",
    page_icon=" ",
    layout='wide'
)
df=pd.read_csv('data\history.csv')


# df = pd.DataFrame(columns=['name','age','color'])
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# config = {
#     'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
#     'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
#     'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
# }

result = st.data_editor(df,num_rows='dynamic')# column_config = config, 

# if st.button('Get results'):
#     st.write(result)