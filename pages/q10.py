import streamlit as st
from pages.utils import get_last_page, get_buttons


st.markdown('### During the recording, three words will be spoken. '
            'Please listen attentively. After the words are played, '
            'you will be prompted to enter the three words on the following screen.')


audio_file = open('three_words.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')

prev_page = get_last_page()
get_buttons(prev_page, 'pages/q11.py')