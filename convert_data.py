import json


with open("instructions.json") as f:
    dict = json.load(f)

with open("instructions.jsonl", 'w') as instruct_json_f:
    for instr in dict["text"]:
        instr = instr.replace("<s>", "").replace("</s>", "").replace('[INST]', '')
        inp, out = instr.split("[/INST]")
        new_instruct = {"instruction": inp, "input": "", "output": out}
        instruct_json_f.write(json.dumps(new_instruct, ensure_ascii=False) + '\n')
