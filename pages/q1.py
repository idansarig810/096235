import streamlit as st
import datetime
from pages.utils import get_buttons

st.title("What day of the week is it today?")
q_1 = st.text_input(label='day of the week', placeholder='type your answer here', label_visibility='hidden', value=None)

get_buttons('main.py', 'pages/q2.py')

st.divider()
today = datetime.date.today()
day_of_week = today.weekday()

# Convert the integer day of the week to a string representation
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
today_name = days[day_of_week]

if q_1 is not None:
    st.markdown('#### The information presented below is exclusively for demonstration purposes.')
    st.markdown(f'**User input:** {q_1}')
    st.markdown(f'**Correct input:** {today_name}')