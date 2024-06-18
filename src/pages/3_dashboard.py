import streamlit as st
import time

# Set page config
st.set_page_config(
    page_title="Dashboarding",
    page_icon="📈",
    layout="wide",
)

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




st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
    