import streamlit as st

st.write("in two")

col1 , col2 = st.columns(2)
with col1:
    one_prev_button = st.button('Previous', key='one_prev_button')
    if one_prev_button:
        st.switch_page('pages/one.py')
with col2:
    one_next_button = st.button('Next', key='one_next_button')
    if one_next_button:
        st.switch_page('pages/three.py')