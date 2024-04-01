import streamlit as st


def get_buttons(prev_page, next_page):
    col1, col2 = st.columns(2)
    with col1:
        one_prev_button = st.button('Previous', key='one_prev_button')
        if one_prev_button:
            st.switch_page(prev_page)
    with col2:
        one_next_button = st.button('Next', key='one_next_button')
        if one_next_button:
            st.switch_page(next_page)


country_dict = {
    'IL': 'Israel',
    'US': 'United States',
    'UK': 'United Kingdom',
    'Aus': 'Australia'
}


def get_country(country):
    return country_dict[country]


results = {
    'q1': None,
    'q2': None,
    'q3': None,
    'q4': None,
    'q5': None,
    'q6': None,
    'q7': None,
    'q8': None,
    'q9': None,
    'q10': None,
}


def get_last_page():
    if results['q6'] is None:
        page = 'q6'
    else:
        if results['q6'] - 7 <= 0:
            page = 'q6'
        else:
            if results['q7'] is None:
                page ='q7'
            else:
                if results['q7']-7<=0:
                    page = 'q7'
                else:
                    if results['q8'] is None:
                        page = 'q8'
                    else:
                        if results['q8']- 7 <= 0:
                            page = 'q8'
                        else:
                            page = 'q9'
    return 'pages/' + page + '.py'


def get_result(key):
    return results[key]


def set_result(key, val):
    results[key] = val
