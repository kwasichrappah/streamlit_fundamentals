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
def load_logistic_regressor_pipeline():
    pipeline = joblib.load(".\\models\\tuned\\best_search_pred.joblib")
    return pipeline

st.cache_resource(show_spinner="Models Loading")
def load_svc_pipeline():
    pipeline = joblib.load(".\\models\\tuned\\best_svc_pred.joblib")
    return pipeline

st.cache_resource(show_spinner="Models Loading")
def load_xgboost_pipeline():
    pipeline = joblib.load(".\\models\\tuned\\best_gs_pred.joblib")
    return pipeline


def select_model():
        col1,col2 = st.columns(2)

        with col2:
             st.selectbox('Select a Model', options = ['CatBoost','Logistic Regressor','XGBoost','SVC'],key='selected_model')

        if st.session_state['selected_model'] == 'CatBoost':
             pipeline = load_catboost_pipeline()
        
        if st.session_state['selected_model'] == 'Logistic Regressor':
             pipeline = load_logistic_regressor_pipeline()

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
    seniorcitizen = st.session_state['seniorcitizen']
    partner = st.session_state['partner']
    dependents = st.session_state['dependents']
    phoneservice = st.session_state['phoneservice']
    multiplelines = st.session_state['multiplelines']
    internetservice = st.session_state['internetservice']
    onlinesecurity = st.session_state['onlinesecurity']
    onlinebackup = st.session_state['onlinebackup']
    deviceprotetion = st.session_state['deviceprotection']
    techsupport = st.session_state['techsupport']
    streamingtv = st.session_state['streamingtv']
    streamingmovies = st.session_state['streamingmovies']
    contract = st.session_state['contract']
    paperlessbilling = st.session_state['paperlessbilling']
    tenure = st.session_state['tenure']
    monthlycharges = st.session_state['monthlycharges']
    totalcharges = st.session_state['totalcharges']

    columns =['seniorcitizen','partner','dependents','phoneservice','multiplelines',
            'internetservice','onlinesecurity','onlinebackup','deviceprotetion',
            'techsupport','streamingtv','streamingmovies','contract','paperlessbilling','monthlycharges','tenure','totalcharges']
    data = [[seniorcitizen,partner,dependents,phoneservice,multiplelines,
            internetservice,onlinesecurity,onlinebackup,deviceprotetion,
            techsupport,streamingtv,streamingmovies,contract,paperlessbilling,monthlycharges,tenure,totalcharges]]
    #create dataframe
    df = pd.DataFrame(data,columns=columns)

    df['PredictionTime'] = datetime.date.today()
    df['Model_used'] = st.session_state['selected_model']

    df.to_csv('.\\data\\history.csv',mode='a',header = not os.path.exists('.\\data\\history.csv'),index=False)

     #Make prediction
    pred = pipeline.predict(df)
    pred = int(pred[0])
    #  pred = pipeline.predict(df)
    #  prediction = int(pred[0])
     ##prediction = encoder.inverse_transform([pred])

     #Get probability
    probability = pipeline.predict_proba(pred)

     #Updating state
    st.session_state['prediction'] = pred
    st.session_state['probability'] = probability

    return pred,probability


def display_form():
     pipeline = select_model()

     with st.form('input-feaatures'):
          col1,col2 = st.columns(2)

          with col1:
               st.write ('### Information 1')
               st.selectbox('Senior Citizen',['Yes','No'],key='seniorcitizen')
               st.selectbox('Gender',['Male','Female'],key='gender')
               st.selectbox('Dependents',['Yes','No'],key='dependents')
               st.selectbox('Partner',['Yes','No'],key='partner')
               st.selectbox('Phone Service',['Yes','No'],key='phoneservice')
               st.selectbox('Multiple Lines',['Yes','No'],key='multiplelines')
               st.selectbox('Internet Service',['Fiber Optic','DSL','No'],key='internetservice')


          with col2:
               st.write('### Information 2')
               st.selectbox('Online Security',['Yes','No'],key='onlinesecurity')
               st.selectbox('Online Backup',['Yes','No'],key='onlinebackup')
               st.selectbox('Device Protection',['Yes','No'],key='deviceprotection')
               st.selectbox('Tech Support',['Yes','No'],key='techsupport')
               st.selectbox('Streaming TV',['Yes','No'],key='streamingtv')
               st.selectbox('Streaming Movies',['Yes','No'],key='streamingmovies')
               st.selectbox('Contract Type',['Month-to-month','One year','Two year'],key='contract')
               st.selectbox('Paperless Billing',['Yes','No'],key='paperlessbilling')
               st.number_input('Enter your monthly charge', key='monthlycharges', min_value=10, max_value=200, step=1)
               st.number_input('Enter Tenure in months', key = 'tenure', min_value=0, max_value=72, step=1)
               st.number_input('Enter your totalcharge', key = 'totalcharges', min_value=10, max_value=1000, step=1)



          st.form_submit_button('Predict', on_click=make_prediction, kwargs=dict(pipeline=pipeline))


def load_catboost_pipeline():
    pipeline = joblib.load("./models/CatBoost.joblib")
    return pipeline
cat_boost = load_catboost_pipeline()
print(cat_boost)



if __name__ == '__main__':
     st.title("Make a Prediction")
     display_form()

     prediction = st.session_state['prediction']
     probability = st.session_state['probability']

     
