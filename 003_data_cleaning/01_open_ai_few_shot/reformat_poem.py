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
                    'Reformat the following purananuru poem to correct structure,
                    "உவவு\\nமதி உருவின் ஓங்கல் வெண் குடை",
                    "நிலவுக்\\nகடல் வரைப்பின் மண்ணகம் நிழற்ற",
                    ",",
                    "ஏம\\nமுரசம் இழுமென முழங்க",
                    ",",
                    "நேமி\\nஉய்த்த நேஎ நெஞ்சின்",
                    ",",
                    "தவிரா\\nஈகை",
                    ",\\n",
                    "கவுரியர் மருக!",
                    "செயிர்\\nதீர் கற்பின் சேயிழை கணவ!",
                    "பொன்\\nஓடைப் புகர் அணி நுதல்",
                    ",",
                    "துன்\\nஅருந் திறல்",
                    ", ",
                    "கமழ் கடாஅத்து",
                    ",",
                    "எயிறு\\nபடையாக எயிற் கதவு இடாஅ",
                    ",",
                    "கயிறு\\nபிணிக்கொண்ட கவிழ் மணி மருங்கின்",
                    ",",
                    "பெருங்\\nகை",
                    ",\\n",
                    "யானை இரும் பிடர்த் தலை இருந்து",
                    ",",
                    "மருந்து\\nஇல் கூற்றத்து அருந் தொழில் சாயாக்",
                    "கருங்\\nகை ஒள் வாட் பெரும்பெயர் வழுதி!",
                    "நிலம்\\nபெயரினும்",
                    ", ",
                    "நின் சொல் பெயரல்",
                    ";",
                    "பொலங்\\nகழற் கால்",
                    ", ",
                    "புலர் சாந்தின்",
                    "விலங்கு\\nஅகன்ற வியல் மார்ப!",
                    "ஊர்\\nஇல்ல",
                    "\\n",
                    "உயவு அரிய",
                    ",",
                    "நீர்\\nஇல்ல",
                    "\\n",
                    "நீள் இடைய",
                    ",",
                    "பார்வல்\\nஇருக்கை",
                    "\\n",
                    "கவி கண் நோக்கின்",
                    ",",
                    "செந்\\nதொடை பிழையா வன்கண் ஆடவர்",
                    "அம்பு\\nவிட",
                    ",\\n",
                    "வீழ்ந்தோர் வம்பப் பதுக்கை",
                    ",",
                    "திருந்து\\nசிறை வளை வாய்ப் பருந்து இருந்து உயவும்",
                    "உன்ன\\nமரத்த துன் அருங் கவலை",
                    ",",
                    "நின்\\nநசை வேட்கையின் இரவலர் வருவர் அது",
                    "முன்னம்\\nமுகத்தின் உணர்ந்து",
                    ", ",
                    "அவர்",
                    "இன்மை\\nதீர்த்தல் வன்மையானே.",
                    "திணை\\nபாடாண் திணை",
                    ";\\n",
                    "துறை செவியறிவுறூஉ",
                    ";",
                    "வாழ்த்தியலும்\\nஆம்."
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

