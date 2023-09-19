from .FREDModel import FREDModel
import torch


class UserDialog:
    def __init__(self, first_prompt: str, model_path: str, device: torch.device) -> None:
        self._dialog = ['<SC1>' + first_prompt + 'Ваш первый диалог:']
        self._first_prompt
        self._model = FREDModel(model_path, device)

    def reply_to_message(self, message: str) -> str:
        self._dialog.append(message)
        prompt = '\n'.join(self._dialog) + ' Твой ответ:<extra_id_0>'
        reply = self._model(prompt)
        return reply
    
    def clear(self) -> None:
        self._dialog = ['<SC1>' + self._first_prompt + 'Ваш первый диалог:']
