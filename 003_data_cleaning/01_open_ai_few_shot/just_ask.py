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
                "content": f"""Give me Purananuru poem 6 with title, poem and its meaning in Tamil in JSON format with title, poem and meaning fields. """
            },
        ],
    )
    return completion.choices[0].message


# NOTE: not working
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

