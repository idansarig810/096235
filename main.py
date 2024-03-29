import streamlit as st

st.title('Welcome to the MMSE test')
st.write(
    "Welcome to our cognitive assessment app. In this questionnaire, you'll be presented with a series "
    "of approximately 25 questions designed to evaluate various aspects of your cognitive abilities. "
    "Simply follow the instructions and respond to each question to the best of your ability.")
st.write(
    "At the conclusion of this assessment, your results will be securely transmitted to your healthcare provider. "
    "In the event that any unusual findings or concerns are identified, your doctor will be promptly notified and"
    " may reach out to discuss further evaluation or interventions.")
_ , col2 = st.columns(2)
with col2:
    intro_next_button = st.button('Next', key='intro_button')
    if intro_next_button:
        st.switch_page('pages/one.py')