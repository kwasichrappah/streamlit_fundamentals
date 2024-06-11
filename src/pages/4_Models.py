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
    pipeline = joblib.load(".\\models\\tuned\\best_catboost_pred.joblib")
    return pipeline

st.cache_resource(show_spinner="Models Loading")
def load_xgboost_pipeline():
    pipeline = joblib.load(".\\models\\tuned\\best_gs_pred.joblib")
    return pipeline

st.cache_resource(show_spinner="Models Loading")
def load_svc_pipeline():
    pipeline = joblib.load(".\\models\\tuned\\best_svc_pred.joblib")
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

def make_prediction(pipeline):
     age = st.session_state['age']
     distancefromhome = st.session_state['distancefromhome']
     department = st.session_state['department']
     education = st.session_state['education']
     educational_field = st.session_state['educationalfield']
     environmental_satisfaction = st.session_state['environmental_satisfaction']
     job_satisfaction = st.session_state['job_satisfaction']
     marital_status = st.session_state['marital_status']
     monthly_income = st.session_state['monthly_income']
     numofcompaniesworked = st.session_state['numofcompaniesworked']
     worklifebalance = st.session_state['worklifebalance']
     yearsatcompany = st.session_state['yearsatcompany']

     columns =['Age','Department','Distancefromhome','Education','EducationField',
               'EnvironmentSatisfaction','JobSatisfaction','MaritalStatus','MonthlyIncome','NumCompaniesWorkedat',
               'WorklifeBalance','YearsAtCompany']
     data = [[age,department,distancefromhome,education,educational_field,
              environmental_satisfaction,job_satisfaction,marital_status,monthly_income,
              numofcompaniesworked,worklifebalance,yearsatcompany]]

def display_form():
     pipeline = select_model()

     with st.form('input-feaatures'):
          col1,col2,col3 = st.columns(3)

          with col1:
               st.write ('### Personal Information')
               st.number_input('Enter your age',min_value=18,max_value=60,step=1,key='age')
               st.number_input('Distance from Home',min_value=10,step=1,key='distancefromhome')
               st.number_input('Monthly Income',min_value=2000,max_value=1000000,step=100,key='monthly_income')
               st.selectbox('Marital Status',['Single','Married','Divorced'],key='marital_status')

          with col2:
               st.write('### Work Information')
               st.selectbox('Enter Department',options=['Sales','Research & Development','Human Resources'],key='department')
               st.selectbox('Enter Educational Field',options=['Life Sciences','Other','Medical','Marketing','Technical Degree','Human Resources'], key='educationalfield')
               st.number_input('Educational Field',min_value=1,max_value=5,step=1,key='education')
               st.number_input('Years at Company',min_value=1,max_value=60,step=1,key='yearsatcompany')

          with col3:
               st.write('### Satisfaction')
               st.number_input('Job Satisfaction',min_value=1,max_value=4,step=1,key='job_satisfaction')
               st.number_input('Environment Satisfaction',min_value=1,max_value=4,step=1,key='environmental_satisfaction')
               st.number_input('Work-Life Balance',min_value=1,max_value=4,step=1,key='worklifebalance')
               st.number_input('Number of Companies worked at',min_value=1,max_value=6,step=1,key='numofcompaniesworked')

          st.form_submit_button('Predict',on_click=make_prediction,kwargs= dict(pipeline = pipeline))


if __name__ == '__main__':
     st.title("Make a Prediction")
     display_form()

     prediction = st.session_state['prediction']
     probability = st.session_state['probability']