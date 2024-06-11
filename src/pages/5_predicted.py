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

st.cache_resource(show_spinner="Models Loading")
def load_catboost_pipeline():
    pipeline = joblib.load("./models\tuned\best_catboost_pred.joblib")
    return pipeline

st.cache_resource(show_spinner="Models Loading")
def load_xgboost_pipeline():
    pipeline = joblib.load("./models\tuned\best_gs_pred.joblib")
    return pipeline

st.cache_resource(show_spinner="Models Loading")
def load_svc_pipeline():
    pipeline = joblib.load("./models\tuned\best_svc_pred.joblib")
    return pipeline

def select_model():
        col1,col2 = st.columns(2)

        with col2:
             st.selectbox('Select a Model', options = ['CatBoost','XGBoost','SVC'])


















df = pd.DataFrame(columns=['name','age','color'])
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
}

result = st.data_editor(df, column_config = config, num_rows='dynamic')

if st.button('Get results'):
    st.write(result)