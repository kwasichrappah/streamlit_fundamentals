import streamlit as st
import time

st.write("Hello,This is my first web app for a ML model")
st.title ("Customer Churn Predictor")
st.markdown("Page 2: Dashboards")



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

#jupyter nbconvert --to script my_notebook.ipynb
