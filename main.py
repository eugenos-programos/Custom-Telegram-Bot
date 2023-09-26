from src import create_bot, UserDialog
import os
from settings import configs
import torch


BOT_TOKEN = os.environ["BOT_TOKEN"]

bot = create_bot(BOT_TOKEN, UserDialog(**configs, device=torch.device("cuda" if torch.cuda.is_available() else "cpu")))
bot.infinity_polling()
