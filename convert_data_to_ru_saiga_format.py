import json


with open("instructions.json") as f:
    dict = json.load(f)

with open("instructions_saiga.jsonl", 'w') as instruct_json_f:
    for instr in dict["text"]:
        new_instruct = {"messages": []}
        instr = instr.replace("<s>", "").replace("</s>", "").replace('[INST]', '')
        inp, out = instr.split("[/INST]")
        new_instruct["messages"].append({"role": "bot", "content": [inp, out]})
        instruct_json_f.write(json.dumps(new_instruct, ensure_ascii=False) + '\n')
