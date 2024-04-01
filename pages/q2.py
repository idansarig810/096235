import streamlit as st
import datetime
from pages.utils import get_buttons

st.title("What numerical month of the year is it currently?")
q_2 = st.number_input(label='month', placeholder='type your answer here', label_visibility='hidden', value=None, step=1)

get_buttons('pages/q1.py', 'pages/q3.py')

st.divider()
today = datetime.date.today()
today_month = today.month

if q_2 is not None:
    st.markdown('#### The information presented below is exclusively for demonstration purposes.')
    st.markdown(f'**User input:** {q_2}')
    st.markdown(f'**Correct input:** {today_month}')

