import json

# Load the JSON data
with open('purananuru_cleaned_attempt_2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Sort the data by the poem_number field
poems = sorted(data, key=lambda x: x['poem_number'])

# Save the sorted data back to the JSON file
with open('puranaanuru_sorted_attempt_3.json', 'w', encoding='utf-8') as file:
    json.dump(poems, file, ensure_ascii=False, indent=4)