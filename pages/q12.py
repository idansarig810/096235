import streamlit as st
from pages.utils import get_buttons
from pages.llama_utils import get_rating

st.title("Whrite one clear and coherent sentence")
q_12 = st.text_input(label='sentence', placeholder='type your answer here', label_visibility='hidden', value=None)

get_buttons('main.py', 'pages/q2.py')

st.divider()
if q_12 is not None:
    rating = get_rating(q_12)
    st.markdown('#### The information presented below is exclusively for demonstration purposes.')
    st.markdown(f'**User input:** {q_12}')
    st.markdown('The scale for coherency ranges from 5 (indicating very high coherence) to 1 (representing no sense at all).')
    st.markdown('An answer is considered good if it meets or exceeds a threshold of 4.')
    st.markdown(f'**The user input sentence coherency score is:** {rating}')