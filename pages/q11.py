import streamlit as st
from st_audiorec import st_audiorec
import wave
import io
from pages.utils import get_last_page
from pages.whisper_utils import transcribe

def save_audio_to_file(audio_data):
    # Create a BytesIO object to store the audio data
    audio_io = io.BytesIO(audio_data)

    # Set the parameters for the WAV file
    with wave.open("first_recorded_audio.wav", "wb") as wav_file:
        wav_file.setnchannels(1)  # Mono channel
        wav_file.setsampwidth(4)  # 2 bytes per sample (16-bit)
        wav_file.setframerate(44000)  # Sample rate
        wav_file.writeframes(audio_io.getvalue())


st.title("Record the words you heard in the previous page's recording.")
st.write('When the icon turns yellow, recording has begun.')

audio_data = st_audiorec()
col1, col2, col3 = st.columns(3)

prev_page = get_last_page()
with col1:
    one_prev_button = st.button('Previous', key='one_prev_button')
    if one_prev_button:
        st.switch_page(prev_page)
with col3:
    one_next_button = st.button('Next', key='one_next_button')
    if one_next_button:
        st.switch_page('pages/q12')

# Check if audio data is recorded
if audio_data:
    # st.audio(audio_data, format='audio/wav')
    with col2:
        # Save the audio data to a WAV file
        save_button = st.button("Save Recording")

    if save_button:
        save_audio_to_file(audio_data)
        st.divider()
        q_11 = transcribe("first_recorded_audio.wav")
        st.markdown('#### The information presented below is exclusively for demonstration purposes.')
        st.markdown(f'**User input:** {q_11}')
        st.markdown(f'**Correct input:** pencil, house, banana')

