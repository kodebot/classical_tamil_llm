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

class Poem(BaseModel):
    poem_number: int
    poem_title: str
    poem_content: list[str]
    poem_meaning: list[str]
    poem_context: list[str]

# Example function to clean text data using OpenAI's GPT-3
def clean_text(new_data):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is helping a user to clean up a text document in Tamil language. Please do NOT make your own meaning or generate text of your own"},
            { 
                "role": "user", 
                "content": f"""
                    Separate the following Aganaanuru poem text to JSON with poem_number, poem_title, poem_content, poem_meaning nad poem_context.
                    The context will include who wrote this poem, who is the subject of the poem and information like year, thinai,etc..
                    Do not make your own data, just use the data from the input and also do not omit any data from the input.
                    <<input-start>>{new_data}<<input-end>>
                """
            },
        ],
        response_format=Poem
    )
    return completion.choices[0].message


## NOTE: Not working - it makes up its own meaning

if __name__ == "__main__":

    with open('aganaanuru_text.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Sort the data by the title field
    cleaned_data = []
    for item in data:
        cleaned_data.append(clean_text(item).content)
        print(f"cleaned {len(cleaned_data)} of {len(data)}\n")
        with open('aganaanuru_cleaned_attempt_3.json', 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

