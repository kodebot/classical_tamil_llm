import json

# Load the JSON data
with open('aganaanuru_cleaned_attempt_2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Sort the data by the poem_number field
poems = sorted(data, key=lambda x: x['poem_number'])

# Save the sorted data back to the JSON file
with open('aganaanuru_sorted_attempt_3.json', 'w', encoding='utf-8') as file:
    json.dump(poems, file, ensure_ascii=False, indent=4)