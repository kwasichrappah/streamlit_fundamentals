import streamlit as st
import pandas as pd
import joblib
import os
import datetime


#setting page title and icon
st.set_page_config(
    page_title = "Prediction Page",
    page_icon = " ",
    layout = 'wide'
)

#Loading the models into streamlit app
st.cache_resource(show_spinner="Models Loading")
def load_catboost_pipeline():
    pipeline = joblib.load('./models/CatBoost.joblib')#("./models/tuned/best_catboost_pred.joblib")
    print(pipeline)
    return pipeline


st.cache_resource(show_spinner="Models Loading")
def load_logistic_regressor_pipeline():
    pipeline = joblib.load('./models/Logistic_Regressor.joblib')#("./models/tuned/best_search_pred.joblib")
    return pipeline


st.cache_resource(show_spinner="Models Loading")
def load_svc_pipeline():
    pipeline = joblib.load('./models/SVM.joblib')#("./models/tuned/best_svc_pred.joblib")
    return pipeline


st.cache_resource(show_spinner="Models Loading")
def load_xgboost_pipeline():
    pipeline = joblib.load('./models/Xgboost.joblib')#("./models/tuned/best_gs_pred .joblib")
    print(pipeline)
    return pipeline

#Selecting model for prediction
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

        #encoder to inverse transform the result
        encoder = joblib.load('./models/encoder.joblib')
        return pipeline,encoder


#Prediction and probability variables state at the start of the webapp
if 'prediction' not in st.session_state:
     st.session_state['prediction'] = None
if 'probability' not in st.session_state:
     st.session_state['probability'] = None


#Making prediction 
def make_prediction(pipeline,encoder):
     SeniorCitizen = st.session_state['SeniorCitizen']
     partner = st.session_state['Partner']
     #gender  = st.session_state['gender'] Not included in my model for prediction
     dependents = st.session_state['Dependents']
     phoneservice = st.session_state['PhoneService']
     multiplelines = st.session_state['MultipleLines']
     InternetService = st.session_state['InternetService']
     onlinesecurity = st.session_state['OnlineSecurity']
     onlinebackup = st.session_state['OnlineBackup']
     deviceprotetion = st.session_state['DeviceProtection']
     techsupport = st.session_state['TechSupport']
     streamingtv = st.session_state['StreamingTV']
     streamingmovies = st.session_state['StreamingMovies']
     contract = st.session_state['Contract']
     paperlessbilling = st.session_state['PaperlessBilling']
     tenure = st.session_state['tenure']
     monthlycharges = st.session_state['MonthlyCharges']
     #totalcharges = st.session_state['totalcharges'] #Not included in my model for prediction
     paymentmethod = st.session_state['PaymentMethod']

     columns = ['seniorcitizen','partner','dependents','phoneservice','multiplelines',
              'internetservice','onlinesecurity','onlinebackup','deviceprotetion',
              'techsupport','streamingtv','streamingmovies','contract','paperlessbilling','paymentmethod','monthlycharges','tenure']
     
     data = [[SeniorCitizen,partner,dependents,phoneservice,multiplelines,
              InternetService,onlinesecurity,onlinebackup,deviceprotetion,
              techsupport,streamingtv,streamingmovies,contract,paperlessbilling,paymentmethod,monthlycharges,tenure]]
     #create dataframe
     df = pd.DataFrame(data,columns=columns)

     df['PredictionTime'] = datetime.date.today()
     df['Model_used'] = st.session_state['selected_model']

     df.to_csv('.\\data\\history.csv',mode='a',header = not os.path.exists('.\\data\\history.csv'),index=False)

     #Make prediction
     
     pred = pipeline.predict(df)
     pred = int(pred[0])
     prediction = encoder.inverse_transform(pred)

     #Get probability
     #probability = pipeline.predict_proba(pred)

     #Updating state
     st.session_state['prediction'] = pred
     #st.session_state['probability'] = probability

     return prediction#,probability

#Display form on the streamlit app to take user input
def display_form():
     pipeline,encoder = select_model()

     with st.form('input-features'):
          col1,col2 = st.columns(2)

          with col1:
               st.write ('### Personal Information')
               st.selectbox('Senior Citizen',['Yes','No'],key='SeniorCitizen')
               #st.selectbox('Gender',['Male','Female'],key='gender')
               st.selectbox('Dependents',['Yes','No'],key='Dependents')
               st.selectbox('Partner',['Yes','No'],key='Partner')
               st.selectbox('Phone Service',['Yes','No'],key='PhoneService')
               st.selectbox('Multiple Lines',['Yes','No'],key='MultipleLines')
               st.selectbox('Internet Service',['Fiber Optic','DSL'],key='InternetService')


          with col2:
               st.write('### Work Information')
               st.selectbox('Online Security',['Yes','No'],key='OnlineSecurity')
               st.selectbox('Online Backup',['Yes','No'],key='OnlineBackup')
               st.selectbox('Device Protection',['Yes','No'],key='DeviceProtection')
               st.selectbox('Tech Support',['Yes','No'],key='TechSupport')
               st.selectbox('Streaming TV',['Yes','No'],key='StreamingTV')
               st.selectbox('Streaming Movies',['Yes','No'],key='StreamingMovies')
               st.selectbox('Contract Type',['Month-to-month','One year','Two year'],key='Contract')
               st.selectbox('Paperless Billing',['Yes','No'],key='PaperlessBilling')
               st.selectbox('What is your payment method', options=['Electronic Check','Mailed check', 'Bank transfer', 'Credit Card']
                            ,key='PaymentMethod')
               st.number_input('Enter your monthly charge', key='MonthlyCharges', min_value=10, max_value=200, step=1)
               st.number_input('Enter Tenure in months', key = 'tenure', min_value=0, max_value=72, step=1)
               #st.number_input('Enter your totalcharge', key = 'totalcharges', min_value=10, max_value=1000, step=1)


          st.form_submit_button('Predict',on_click = make_prediction,kwargs = dict(pipeline = pipeline,encoder=encoder))


if __name__ == '__main__':
     st.title("Make a Prediction")
     display_form()
     st.write(st.session_state)

     