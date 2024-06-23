import streamlit as st
import time
import plotly.express as px



def loader():
  'Starting a long computation...'
  # Add a placeholder
  latest_iteration = st.empty()
  bar = st.progress(0)

  for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

  '...and now we\'re done!'


def eda_dashboard():
   st.markdown('### Exploratory Data AnalyDashboard')

def kpi_dashboard():
   st.markdown ('### Key Performance Indicators')

#st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})


if __name__ == '__main__':
   
   st.title("Dashboard")

   col1,col2 = st.columns(2)
   with col1:
      pass
   with col2:
      st.selectbox('Select the type of Dashboard',options=['EDA','KPI'],key='dashboard_type')

   if st.session_state['dashboard_type'] == 'EDA':
    eda_dashboard()

   else:
    kpi_dashboard()
