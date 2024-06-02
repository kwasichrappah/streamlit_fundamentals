import streamlit as st
import pandas as pd
import matplotlib as plt
import sqlalchemy as sa
import pyodbc  
from dotenv import dotenv_values 


st.title ("Data of Customers")
st.subheader("This is a breakdown of customer attrition attributes")

#Creation of Connection to Database



# #Access protocols for the SQL Database
# env_variables= dotenv_values('logins.env')
# database= env_variables.get('database')
# server = env_variables.get('server')
# username = env_variables.get('username')
# password = env_variables.get('password')

# #Creation of Connection to Database
# connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};MARS_Connection=yes;MinProtocolVersion=TLSv1.2;"
# #connection = pyodbc.connect(connection_string)
# conn = sa.create_engine(connection_string)


# #Querying SQL Database and reading the table into a dataframe
# query = "SELECT * FROM LP2_Telco_churn_first_3000"

# # Function to fetch data from the database
# def get_data(query):
#     with conn.connect() as connection:
#         result = pd.read_sql(query, connection)
#     return result



# #sql_df= pd.read_sql(query, connection)


