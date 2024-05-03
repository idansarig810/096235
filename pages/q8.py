import streamlit as st
from pages.utils import get_buttons
from pages.utils import get_result, set_result

q_7 = get_result('q7')
# same logic as in page q7
if q_7 is None:
    st.switch_page('pages/q10.py')
if q_7-7 < 0:
    st.switch_page('pages/q10.py')


st.title(f"Calculate and answer: {q_7}-7=____")
q_8 = st.number_input(label='year',
                      placeholder='type your answer here',
                      label_visibility='hidden',
                      value=None,
                      step=1,
                      max_value=q_7)
ans = q_7-7

get_buttons('pages/q7.py', 'pages/q9.py')

st.divider()
if q_8 is not None:
    set_result('q8', q_8) # saves result in utils results
    st.markdown('#### The information presented below is exclusively for demonstration purposes.')
    st.markdown(f'**User input:** {q_8}')
    st.markdown(f'**Correct input:** {q_7}-7={ans}')

