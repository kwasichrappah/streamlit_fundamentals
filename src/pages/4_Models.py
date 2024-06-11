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
             st.selectbox('Select a Model', options = ['CatBoost','XGBoost','SVC'],key='selected_model')

        if st.session_state['selected_model'] == 'CatBoost':
             pipeline = load_catboost_pipeline()
        
        if st.session_state['selected_model'] == 'XGBoost':
             pipeline = load_xgboost_pipeline()
        else:
             pipeline = load_svc_pipeline()

        #ENCODER///////////////////////////

        return pipeline

if 'prediction' not in st.session_state:
     st.session_state['prediction']= None
if 'probability' not in st.session_state:
     st.session_state['probability']= None
