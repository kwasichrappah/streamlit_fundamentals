import streamlit as st
import pandas as pd
import matplotlib as plt
import pyodbc  


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

st.write(rows)
