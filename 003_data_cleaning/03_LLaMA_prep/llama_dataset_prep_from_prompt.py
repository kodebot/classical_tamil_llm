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
    with open('../../004_datasets/Finetuning/full_web_traning_and_test/full_web_training.jsonl', 'r', encoding='utf-8') as file:
        for line in file:
            jline = json.loads(line)
            result.append( f"""<s>[INST]{jline['prompt']}[/INST]{jline['completion']}</s>\n""")

    with open('full_web_training_llama.txt', 'w', encoding='utf-8') as f:
        f.writelines(result)