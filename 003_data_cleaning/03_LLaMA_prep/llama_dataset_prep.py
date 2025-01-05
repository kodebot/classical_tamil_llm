import os
import json

if __name__ == "__main__":

    # result = []
    # with open('../../004_datasets/Agananuru/aganaanuru_web.json', 'r', encoding='utf-8') as file:
    #     data = json.load(file)
    #     for line in data:
    #         poem_number = f"இது அகநானூறு பாடல் {line["poem_number"]} "
    #         poem_meaning = f"இந்த பாடலின் பொருள்: {" ".join(line["poem_meaning"])}"
    #         poem_context = f"இந்த பாடல் சம்பந்தமான சில தகவல்கள்: {" ".join(line["poem_context"])}"
    #         poem = " ".join(line["poem_content"])
    #         result.append( f"""<s>[INST]{poem}[/INST]{poem_number} {poem_meaning} {poem_context}</s>\n""")

    # with open('aganaanuru_llama_inst.txt', 'w', encoding='utf-8') as f:
    #     f.writelines(result)


    result = []
    with open('../../004_datasets/Purananuru/puranaanuru_web.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for line in data:
            poem_number = f"இது புறநானூறு பாடல் {line["poem_number"]} "
            poem_meaning = f"இந்த பாடலின் பொருள்: {" ".join(line["poem_meaning"])}"
            poem_context = f"இந்த பாடல் சம்பந்தமான சில தகவல்கள்: {" ".join(line["poem_context"])}"
            poem = " ".join(line["poem_content"])
            result.append( f"""<s>[INST]{poem}[/INST]{poem_number} {poem_meaning} {poem_context}</s>\n""")

    with open('purananuru_llama_inst.txt', 'w', encoding='utf-8') as f:
        f.writelines(result)