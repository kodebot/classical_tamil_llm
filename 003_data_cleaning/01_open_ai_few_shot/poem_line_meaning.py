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
                    'Matching poem_meaning to each line of the poem_content, do not make up your own meaning and provide the result in JSON format with poem line and its corresponding meaning,
                    "poem_content": [
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
                    ],
                    "poem_meaning": [
                        "தலையில் கொன்றைப் பூ சூடியவன்.",
                        "மார்பில் கொன்றை-மாலை அணிந்தவன்.",
                        "அவனுக்கு ஊர்தி வெண்ணிறக் காளைமாடு.",
                        "கொடியும் காளைமாடு என்று கூறுகின்றனர்.",
                        "தொண்டையில் நஞ்சு தேங்கிய கறை.",
                        "அந்தக் கறை அந்தணர் மறையில் போற்றப்படுகிறது.",
                        "ஒருபாதி (இடப்புறம்) பெண்-உருவம்.",
                        "அதனை அவன் தனக்குள் மறைத்துக்கொள்வதும் உண்டு.",
                        "நெற்றியில் பிறை.",
                        "அந்தப் பிறை 18 வகையான தேவ கணங்களாலும் போற்றி வணங்கப்படும்.",
                        "அவன் எல்லா உயிரிங்களுக்கும் பாதுகாவலாக விளங்குபவன்.",
                        "நீர் வற்றாத கரகத்தைக் கையில் வைத்திருப்பவன்.",
                        "தாழ்ந்த சடைமுடியிலும் நீர் வற்றுவதில்லை.",
                        "இந்தக் கோலத்தில் அவன் தவம் செய்துகொண்டிருக்கிறான்."
                    ],
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

