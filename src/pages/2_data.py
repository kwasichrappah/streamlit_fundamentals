import streamlit as st
import pandas as pd
import matplotlib as plt
import pyodbc  
import joblib


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

connection = init_connection()

@st.cache_data(show_spinner = 'running query ...')
def running_query(query):
     with connection.cursor() as cursor:
                            cursor.execute(query)
                            rows = cursor.fetchall()
                            df = pd.DataFrame.from_records(rows, columns = [column[0] for column in cursor.description])

     return df

query = "SELECT * FROM LP2_Telco_churn_first_3000"

rows = running_query(query)

csv_df = pd.read_csv("C:\\Users\\chrap\\OneDrive - ECG Ghana\\Emmanuel Chrappah\\Azubi Africa\\git_hub_repos\\Custormer-Churn\\data\\LP2_Telco-churn-second-2000.csv")
com_df=pd.concat([rows,csv_df],ignore_index=True)

st.write("Sample Data")
st.dataframe(com_df.style.background_gradient(cmap='Blues'), height=600,width=600
             
             
             
             )

























# categoricals = [column for column in com_df.columns if com_df[column].dtype == "O"]

# #column = st.selectbox('Select feature to filter on', categoricals)
# #city_filter = st.selectbox('Select city', options=['All'] + com_df.columns.tolist())
# columns_filter = st.multiselect('Select feature to filter on#', options=categoricals)

# # Select specific column to display
# filtered_df = com_df[[columns_filter]]


# st.dataframe(filtered_df.style.background_gradient(cmap='Blues'), height=300)


#min_val, max_val = st.slider('Select range of values', min(com_df[column]), max(com_df[column]), (min(com_df[column]), max(com_df[column])))
# filtered_df = com_df[(com_df[column] >= min_val) & (df[column] <= max_val)]
# st.dataframe(filtered_df)
