import streamlit as st
import pandas as pd
import matplotlib as plt
import pyodbc  
import joblib
import sys
import numpy as np
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


# Streamlit page configuration
st.set_page_config(page_title="Data", page_icon="💾", layout="wide")


#Creation of Connection to Database

@st.cache_resource(show_spinner = 'connecting to database...')
def init_connection():
    return pyodbc.connect(
            "DRIVER={SQL Server};SERVER="
            + st.secrets["server"]
            + ";DATABASE="
            + st.secrets["database"]
            + ";UID="
            + st.secrets["username"]
            + ";PWD="
            + st.secrets["password"]
            
    
    )


@st.cache_data(show_spinner = 'running query ...')
def running_query(query):
    with connection.cursor() as cursor:
                            cursor.execute(query)
                            rows = cursor.fetchall()
                            df = pd.DataFrame.from_records(rows, columns = [column[0] for column in cursor.description])

    return df


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

if __name__ == "__main__":

    
   authenticator = stauth.Authenticate(
   config['credentials'],
   config['cookie']['name'],
   config['cookie']['key'],
   config['cookie']['expiry_days'],
   config['pre-authorized']
   )


authenticator.login(location='sidebar')

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    connection = init_connection()





    query = "SELECT * FROM LP2_Telco_churn_first_3000"

    rows = running_query(query)

    csv_df = pd.read_csv("C:\\Users\\chrap\\OneDrive - ECG Ghana\\Emmanuel Chrappah\\Azubi Africa\\git_hub_repos\\Custormer-Churn\\data\\LP2_Telco-churn-second-2000.csv")
    com_df=pd.concat([rows,csv_df],ignore_index=True)

    # Load the function from the file
    com_df['TotalCharges'] = pd.to_numeric(com_df['TotalCharges'], errors='coerce')
    com_df=com_df.reset_index()
        #Dropping the index column
    com_df = com_df.drop(['index'], axis = 1 )
    com_df.replace(['No','No internet service','false','No phone service'], "False", inplace = True)

    com_df.replace('Yes',"True", inplace = True)
    com_df['SeniorCitizen'] = np.where(com_df['SeniorCitizen'] == 1, True, False)
    com_df['InternetService']=com_df.InternetService.replace('false','None')
    com_df.replace(['No','No internet service','false','No phone service'], "False", inplace = True)
    com_df.replace('Yes',"True", inplace = True)
    com_df['SeniorCitizen'] = np.where(com_df['SeniorCitizen'] == 1, True, False)
    com_df.InternetService.replace('false','None')
    com_df.replace({'True': True, 'False': False}, inplace = True)



    st.header("Collection of data from AirTigo Telecommunications")

    col1, col2 = st.columns(2)
    with col2:
        option = st.selectbox('Select interested category...', options=["All", "Numerical", "Categorical","Boolean"])

    cat = com_df.select_dtypes(include='object').columns.tolist()
    num = com_df.select_dtypes(include='number').columns.tolist()
    bool = com_df.select_dtypes(include='bool').columns.tolist()

    if option == 'Categorical':
        filtered_df = com_df[cat]
    elif option == 'Numerical':
              filtered_df = com_df[num]
    elif option == 'Boolean':
            filtered_df = com_df[bool]          
    else:
            filtered_df = com_df


    with st.container(border = True,height = 650):
        st.dataframe(filtered_df.style.background_gradient(cmap='Blues'), height=600,width=600,use_container_width= True,hide_index=True
                
                
                
                )
    st.caption('Data was gathered from :blue[an SQL database and a CSV file]')


    
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
