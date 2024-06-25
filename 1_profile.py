import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader



# Set page config
st.set_page_config(
    page_title="Profile",
    page_icon="🛖",
    layout="wide",
)


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


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
    st.title ("Customer Churn Predictor WebApp")
    st.write("This is a ML model application that predicts whether a customer will curn or not.")
    st.write("It uses ML algorithms to make these predictions.")
    tab1, tab2, tab3 = st.tabs(["Problem Statement","Key Features", "Key Metrics and Success Criteria"])

    with tab1:
        st.subheader('Problem Statement', divider='red')
        st.subheader("This project aims to :rainbow[predict customer churn] for a telecommunications company.")
        st.markdown("In the telecom industry, customers are able to choose from multiple service providers and actively switch from one operator to another.\
                    In this highly competitive market, the telecommunications industry experiences an average of 15-25% \
                    annual churn rate. Given the fact that it costs 5-10 times more to acquire a new customer than to retain an existing one,\
                    customer retention has now become even more important than customer acquisition.")
        
    with tab2:
       st.subheader('Key Features in the model', divider='orange')
       st.markdown("- Customer demographics ")
       st.markdown("- Services subscribed ")
       st.markdown("- Contract details ")
       st.markdown("- Usage patterns ")
       st.markdown("- Churn status ")

    with tab3:
       st.subheader("Key Metrics and Success Criteria",divider = "green")
       st.markdown("• Model Accuracy : The ability of the machine learning model to accurately predict customer churn.")
       st.markdown("• Model Interpretability : The degree to which the model’s predictions and insights can be understood and utilized by stakeholders.")
       st.markdown("• Business Impact : The effectiveness of retention strategies implemented based on the model’s recommendations in reducing customer churn rates and improving overall customer satisfaction and retention.")

    
    # Inject custom CSS for styling
    st.markdown(
        """
        <style>
        .custom-text {
            font-size: 12px; /* Adjust the font size as needed */
            text-align: right;
            color: #000; /* Optionally, you can also change the text color */
            margin: 0; /* Adjust margin as needed */
            padding: 0; /* Adjust padding as needed */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create text input and apply custom class
    user_input = 'Created by Emmanuel Chrappah'

    # Apply the custom class to the displayed text
    st.markdown(f'<p class="custom-text">{user_input}</p>', unsafe_allow_html=True)

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')








# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How I can be contacted?',
    ('chrappahkwasi@gmail.com','chrappahkwasi@gmail.com', '0209100603')
)
        





















#streamlit run "c:/Users/chrap/OneDrive - ECG Ghana/Emmanuel Chrappah/Azubi Africa/git_hub_repos/streamlit_fundamentals/src/app.py"     