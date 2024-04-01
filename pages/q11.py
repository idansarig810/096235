import streamlit as st
from audio_recorder_streamlit import audio_recorder
import wave
import io
from pages.utils import get_buttons, get_last_page

def save_audio_to_file(audio_data):
    # Create a BytesIO object to store the audio data
    audio_io = io.BytesIO(audio_data)

    # Set the parameters for the WAV file
    with wave.open("first_recorded_audio.wav", "wb") as wav_file:
        wav_file.setnchannels(1)  # Mono channel
        wav_file.setsampwidth(4)  # 2 bytes per sample (16-bit)
        wav_file.setframerate(41000)  # Sample rate
        wav_file.writeframes(audio_io.getvalue())


st.title("Record the words you heard in the previous page's recording.")
st.write('When the icon turns yellow, recording has begun.')
_, col2, _ = st.columns(3)
# Display the audio recorder widget
with col2:
    audio_data = audio_recorder(
        sample_rate=41_000,
        text='',
        recording_color="#e8b62c",
        neutral_color="#6aa36f",
        icon_name="user",
        icon_size="3x"
    )

# Check if audio data is recorded
if audio_data:
    st.audio(audio_data, format='audio/wav')

    # Save the audio data to a WAV file
    save_audio_to_file(audio_data)

    if st.button("Save Recording"):
        print("button clicked")


prev_page = get_last_page()
get_buttons(prev_page, 'pages/q12')