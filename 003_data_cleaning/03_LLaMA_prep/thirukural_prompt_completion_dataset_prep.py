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
    with open('../../004_datasets/Thirukural/thirukurals_ta.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for aadhikaram in data:
            for kural in aadhikaram["kurals"]:
                poem_number = f"இது ் திருக்குறள் {kural["kuralNo"]} "
                poem_meaning = "இந்த பாடலின் பொருள்: "
                for exp in kural["explanations"]:
                    poem_meaning = poem_meaning + f"ஆசிரியர்: {exp['author']}, பொருள்:{exp['explanation']}"
                poem_context = f"இந்த பாடல் சம்பந்தமான சில தகவல்கள்: அதிகாரம்:{aadhikaram["aadhikaramNo"]}, {aadhikaram["adhikaramName"]}, பால்: {aadhikaram["paal"]}"
                poem = kural["kural"].replace("\n", "")
                result.append( f"""{{"prompt": "{poem}", "completion": "{poem_number} {poem_meaning} {poem_context}"}}\n""")

    with open('thirukural_prompt_completion_inst.txt', 'w', encoding='utf-8') as f:
        f.writelines(result)