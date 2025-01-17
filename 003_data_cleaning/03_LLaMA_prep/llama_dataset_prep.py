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
    with open('aganaanuru_web.json', 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)
        with open('aganaanuru_upsample.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for line in data:
                line1 = [x for x in data1 if x["poem_number"] == line["poem_number"] ][0]
                print(line1)
                poem_number = f"இது அகநானூறு பாடல்் {line["poem_number"]} "
                poem_meaning = f"இந்த பாடலின் பொருள்: {" ".join(line["poem_meaning"])}"
                poem_context = f"இந்த பாடல் சம்பந்தமான சில தகவல்கள்: {" ".join(line1["poem_context"])}"
                poem = " ".join(line1["poem_content"])
                result.append( f"""<s>[INST]{poem}[/INST]{poem_number} {poem_meaning} {poem_context}</s>\n""")

        with open('aganaanuru_llama_inst_upsampled.txt', 'w', encoding='utf-8') as f:
            f.writelines(result)