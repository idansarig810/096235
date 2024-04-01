import streamlit as st
import datetime
from pages.utils import get_buttons

st.title("What is the current year?")
q_3 = st.number_input(label='year',
                      placeholder='type your answer here',
                      label_visibility='hidden',
                      value=None,
                      step=1,
                      min_value=1900)

get_buttons('pages/q2.py', 'pages/q4.py')

st.divider()
today = datetime.date.today()
today_year = today.year

if q_3 is not None:
    st.markdown('#### The information presented below is exclusively for demonstration purposes.')
    st.markdown(f'**User input:** {q_3}')
    st.markdown(f'**Correct input:** {today_year}')

