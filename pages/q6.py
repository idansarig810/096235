import streamlit as st
from pages.utils import get_buttons
from pages.utils import set_result


st.title("Calculate and answer: 33-7=____")
q_6 = st.number_input(label='year',
                      placeholder='type your answer here',
                      label_visibility='hidden',
                      value=None,
                      step=1,
                      max_value=100)

get_buttons('pages/q5.py', 'pages/q7.py')

st.divider()

if q_6 is not None:
    set_result('q6', q_6) # saves result in utils results
    st.markdown('#### The information presented below is exclusively for demonstration purposes.')
    st.markdown(f'**User input:** {q_6}')
    st.markdown(f'**Correct input:** 33-7=26')

