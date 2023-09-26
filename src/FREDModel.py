from peft import PeftModel
import torch
import transformers


class FREDModel:
    def __init__(self, path: str, device: torch.device) -> None:
        model = transformers.T5ForConditionalGeneration.from_pretrained(path, load_in_8bit=True, device_map="auto")
        self._tokenizer = transformers.GPT2Tokenizer.from_pretrained(path)
        self._tokenizer.add_special_tokens({'bos_token': '<s>', 'eos_token': '</s>', 'pad_token': '<pad>'})
        self._model = PeftModel.from_pretrained(model, path, device_map='auto', torch_dtype=torch.float16)
        self._model.eval()
        self.device = device
        print("PEFT model loaded")

    def __call__(self, prompt: str) -> str:
        input_ids = self._tokenizer(prompt, return_tensors='pt').input_ids.to(self.device)
        out_ids = self._model.generate(input_ids=input_ids,
                                    max_length=250,
                                    eos_token_id=self._tokenizer.eos_token_id,
                                    early_stopping=True,
                                    do_sample=True,
                                    temperature=0.8,
                                    top_k=50,
                                    top_p=0.85)
        output = self._tokenizer.decode(out_ids[0][1:]).replace('<extra_id_0>','')
        if '</s>' in output:
            output = output[:output.find('</s>')].strip()
        return output
