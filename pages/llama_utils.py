from openai import OpenAI
import sys

apiKey = sys.argv[1]

client = OpenAI(
    api_key=apiKey,
    base_url="https://api.llama-api.com"
)

def get_rating(sentence):
    print(sentence)
    response = client.chat.completions.create(
        model="llama-13b-chat",
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
            {"role": "user", "content": "This message contains two parts: instructions and a sentence. "
                                        "The sentence will appear after three # signs. "
                                        
                                        "Rate the sentence on a scale of 1 to 5 based on its coherence."
                                        "Only input the number that represents your rating; "
                                        "do not include any additional information; "
                                        "Here's a definition for the scale:"
                                        
                                        "Rating 5: A sentence that makes sense and is coherent in its meaning, "
                                        "demonstrating clear understanding and communication."
                                        
                                        "Rating 4: A sentence that mostly makes sense but may have minor grammatical "
                                        "or structural issues that do not significantly impact understanding."
                                        
                                        "Rating 3: A sentence that is somewhat confusing or ambiguous, "
                                        "with noticeable errors or lack of clarity in its meaning."
                                        
                                        "Rating 2: A sentence that is difficult to understand or contains major errors, "
                                        "making it challenging to decipher the intended message."
                                        
                                        "Rating 1: A sentence that makes no sense at all, lacking coherence or logical "
                                        "connection between its components.."

                                        f"### {sentence}"}
        ]

    )
    rating = response.choices[0].message.content
    return rating
