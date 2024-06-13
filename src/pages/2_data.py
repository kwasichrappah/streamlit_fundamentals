import streamlit as st
import pandas as pd
import matplotlib as plt
import pyodbc  
import joblib
import sys
import numpy as np


if __name__ == "__main__":
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

#streamlit run "c:/Users/chrap/OneDrive - ECG Ghana/Emmanuel Chrappah/Azubi Africa/git_hub_repos/streamlit_fundamentals/src/pages/2_data.py"  