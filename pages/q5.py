import streamlit as st
from pages.utils import get_buttons, get_country, set_result
import geocoder


st.title("Which country are you currently located in?")
q_5 = st.text_input(label='country', placeholder='type your answer here', label_visibility='hidden', value=None)

get_buttons('pages/q4.py', 'pages/q6.py')

st.divider()

g = geocoder.ip('me')
country = g.country
decoded_country = get_country(country)


if q_5 is not None:
    set_result('q5', q_5)
    st.markdown('#### The information presented below is exclusively for demonstration purposes.')
    st.markdown(f'**User input:** {q_5}')
    st.markdown(f'**Correct input:** {decoded_country}')
    st.write('    The current location is obtained from the IP address; for mobile development, the location will be obtained from GPS access.')