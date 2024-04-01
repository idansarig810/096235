import whisper
import torch

# Load the model (make sure to specify the correct model size if needed)
MODEL_PATH = "tiny.pt"
model = whisper.load_model(MODEL_PATH)

# Load your custom weights into the model
model.load_state_dict(torch.load(MODEL_PATH)['model_state_dict'])
device = 'cpu'


class DecodingOptionsWhisper:
    # language that the audio is in; uses detected language if None
    language = 'English'

    # sampling-related options
    temperature = 0.0
    sample_len = None  # maximum number of tokens to sample
    best_of = None  # number of independent sample trajectories, if t > 0
    beam_size = None  # number of beams in beam search, if t == 0
    patience = None  # patience in beam search (arxiv:2204.05424)

    # "alpha" in Google NMT, or None for length norm, when ranking generations
    # to select which to return among the beams or best-of-N samples
    length_penalty = None

    # text or tokens to feed as the prompt or the prefix; for more info:
    # https://github.com/openai/whisper/discussions/117#discussioncomment-3727051
    prompt = None  # for the previous context
    prefix = None  # to prefix the current context

    # list of tokens ids (or comma-separated token ids) to suppress
    # "-1" will suppress a set of symbols as defined in `tokenizer.non_speech_tokens()`
    suppress_tokens = "-1"
    suppress_blank = True  # this will suppress blank outputs
    if device == 'cpu':
        fp16 = False  # use fp16 for most of the calculation
    else:
        fp16 = True

    def get_variables_dict(self):
        """
        Returns a dictionary containing all variables of the class instance.
        """
        return {k: v for k, v in self.__class__.__dict__.items() if not k.startswith('__') and not callable(v)}


decoding_options_dict = {**DecodingOptionsWhisper().get_variables_dict()}


def transcribe(path, lang=None):
    audio = whisper.load_audio(path)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(device)
    # load the options in the configurator
    options_config_dict = decoding_options_dict
    # define the task
    options_config_dict['task'] = 'transcribe'
    options = whisper.DecodingOptions(**decoding_options_dict)

    result = whisper.decode(model, mel, options)
    text = result.text
    return text


def parse_string(string):
    # Split the string based on spaces and commas followed by a space
    words = [word.strip() for word in string.replace(",", " ").split()]

    return words


# Example usage
input_string = transcribe('first_recorded_audio_ilaccent.wav')
parsed_words = parse_string(input_string)
print(parsed_words)
print(input_string)
