import json

# Load the JSON data
with open('puranaanuru_text.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Sort the data by the title field
titles = []
for item in data:
    titles.append(int(item['title'].replace('புறநானூறு', '').strip()))

titles = sorted(titles)

# Save the sorted data back to the JSON file
with open('puranaanuru_text1.json', 'w', encoding='utf-8') as file:
    json.dump(titles, file, ensure_ascii=False, indent=4)