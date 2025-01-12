import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import json

load_dotenv()

# Initialize OpenAI API client
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def reformat_poem():
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful Tamil classic literature and poems expert assistant who is helping a user to clean up a text document in Tamil language."},
            { 
                "role": "user", 
                "content": f"""
                    'Provide very detailed, easy to understand, line by line meaning for the following Poem in Tamil. Meaning should be in Tamil, not English,
                        "கண்ணி கார் நறுங் கொன்றை; காமர்",
                        "வண்ண மார்பின் தாரும் கொன்றை:",
                        "ஊர்தி வால் வெள் ஏறே; சிறந்த",
                        "சீர் கெழு கொடியும் அவ் ஏறு என்ப:",
                        "கறை மிடறு அணியலும் அணிந்தன்று; அக் கறை",
                        "மறை நவில் அந்தணர் நுவலவும் படுமே:",
                        "பெண் உரு ஒரு திறன் ஆகின்று; அவ் உருத்",
                        "தன்னுள் அடக்கிக் கரக்கினும் கரக்கும்:",
                        "பிறை நுதல் வண்ணம் ஆகின்று; அப் பிறை",
                        "பதினெண் கணனும் ஏத்தவும் படுமே",
                        "எல்லா உயிர்க்கும் ஏமம் ஆகிய,",
                        "நீர் அறவு அறியாக் கரகத்து,",
                        "தாழ் சடைப் பொலிந்த, அருந் தவத்தோற்கே."
                """
            },
        ],
    )
    return completion.choices[0].message


# Example usage
if __name__ == "__main__":
    print(reformat_poem().content)

    # with open('aganaanuru_text.json', 'r', encoding='utf-8') as file:
    #     data = json.load(file)

    # # Sort the data by the title field
    # cleaned_data = []
    # for item in data:
    #     cleaned_data.append(clean_text(item).content)
    #     print(f"cleaned {len(cleaned_data)} of {len(data)}\n")
    #     with open('aganaanuru_cleaned.json', 'w', encoding='utf-8') as f:
    #         json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

