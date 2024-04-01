import streamlit as st
import datetime
from pages.utils import get_buttons

st.title("What is the current season in israel?")
q_4 = st.text_input(label='season', placeholder='type your answer here', label_visibility='hidden', value=None)

get_buttons('pages/q3.py', 'pages/q5.py')

st.divider()

today = datetime.date.today()
today_month = today.month
if 11 >= today_month >= 9:
    season = 'Autumn'
elif 8 >= today_month >= 6:
    season = 'Summer'
elif 5 >= today_month >= 3:
    season = 'Spring'
else:
    season = 'Winter'


if q_4 is not None:
    st.markdown('#### The information presented below is exclusively for demonstration purposes.')
    st.markdown(f'**User input:** {q_4}')
    st.markdown(f'**Correct input:** {season}')
    st.write('notice: the question refers to israel due to the different seasons definitions in different locations, '
             'in the future the question will be relevant to the current location of the user')
