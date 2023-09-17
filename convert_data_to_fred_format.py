import json 


with open("instructions_llama.json") as f:
    dict = json.load(f)

with open("instructions_fred.jsonl", 'w') as instruct_json_f:
    for instr in dict["text"]:
        new_instruct = {}
        instr = instr.replace("<s>", "").replace("</s>", "").replace('[INST]', '')
        inp, out = instr.split("[/INST]")
        new_instruct["context"] = inp
        new_instruct["response"] = out
        instruct_json_f.write(json.dumps(new_instruct, ensure_ascii=False) + '\n')
