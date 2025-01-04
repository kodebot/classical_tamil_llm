import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import json

load_dotenv()

class PoemUpSample(BaseModel):
    poem_number: int
    poem_meaning: list[str]

# Initialize OpenAI API client
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def get_meaning(poem):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful Tamil classic literature and poems expert assistant who is helping a user to get the meaning of Tamil classical poems in modern Tamil."},
            { 
                "role": "user", 
                "content": f"""Provide a very detailed and descriptive meaning of this poem - {poem}"""
            },
        ],
        response_format=PoemUpSample
    )
    return completion.choices[0].message


# Example usage
if __name__ == "__main__":

    with open('../../004_datasets/Agananuru/aganaanuru_web.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    upsampled = []
    for item in data:
        if item["poem_number"] < 143:
            continue

        input = f""""poem_number":{item["poem_number"]}, "poem_content": {item["poem_content"]}"""
        upsampled.append(get_meaning(input).content)
        print(f"cleaned {len(upsampled)} of {len(data)}\n")
        with open('aganaanuru_upsample2.json', 'w', encoding='utf-8') as f:
            json.dump(upsampled, f, ensure_ascii=False, indent=4)



