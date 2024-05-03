import streamlit as st
from pages.utils import get_buttons
from pages.utils import get_result, set_result

# if the previous calculation is None, jump to the next question (page 10)
q_6 = get_result('q6')
if q_6 is None:
    st.switch_page('pages/q10.py')

# if the result in the previous question is smaller than 7, jump to the next question (page 10)
if q_6 - 7 < 0:
    st.switch_page('pages/q10.py')

st.title(f"Calculate and answer: {q_6}-7=____")
q_7 = st.number_input(label='year',
                      placeholder='type your answer here',
                      label_visibility='hidden',
                      value=None,
                      step=1,
                      max_value=q_6)
ans = q_6 - 7

get_buttons('pages/q6.py', 'pages/q8.py')

st.divider()
if q_7 is not None:
    set_result('q7', q_7)  # saves result in utils results
    st.markdown('#### The information presented below is exclusively for demonstration purposes.')
    st.markdown(f'**User input:** {q_7}')
    st.markdown(f'**Correct input:** {q_6}-7={ans}')
