import streamlit as st
from pages.utils import get_buttons
from pages.utils import get_result, set_result

q_8 = get_result('q8')
# same logic as in page q7
if q_8 is None:
    st.switch_page('pages/q10.py')
if q_8-7 < 0:
    st.switch_page('pages/q10.py')


st.title(f"Calculate and answer: {q_8}-7=____")
q_9 = st.number_input(label='year',
                      placeholder='type your answer here',
                      label_visibility='hidden',
                      value=None,
                      step=1,
                      max_value=q_8)
ans = q_8-7

get_buttons('pages/q7.py', 'pages/q10.py')

st.divider()
if q_9 is not None:
    set_result('q9', q_9) # saves result in utils results
    st.markdown('#### The information presented below is exclusively for demonstration purposes.')
    st.markdown(f'**User input:** {q_9}')
    st.markdown(f'**Correct input:** {q_8}-7={ans}')

