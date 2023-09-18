import json
import sys


def insert_instruction(question, answer, file):
    question = '<s>[INST]' + question + '[/INST]'
    answer += '</s>'
    text = question + answer
    with open(file, 'r') as js_file:
        json_file_dict = json.load(js_file)
    json_file_dict['text'].append(text)
    with open(file, 'w') as js_file:
        json.dump(json_file_dict, js_file, ensure_ascii=False)


theme = input("set context\n")

while True:
    print('\nquestion:\n')
    question = sys.stdin.read()
    question = question.replace('\n', ' ')
    if not question:
        continue
    print('\nanswer:\n')
    answer = sys.stdin.read()
    answer = answer.replace('\n', ' ')
    if not answer:
        continue
    js_file = 'instructions_llama.json'
    insert_instruction(theme + '.' + question, answer, js_file)
