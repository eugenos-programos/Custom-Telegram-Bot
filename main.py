from src import create_bot, UserDialog
import os
from dotenv import load_dotenv
from settings import configs
import torch


load_dotenv("settings/key.env")
BOT_TOKEN = os.environ["BOT_TOKEN"]

bot = create_bot(BOT_TOKEN)
user_dialog = UserDialog(**configs, device=torch.device("cuda" if torch.cuda.is_available() else "cpu"))

@bot.message_handler(func=lambda msg: True)
def reply_to_message(message):
    reply = ...
    bot.reply_to(message, reply)

bot.infinity_polling()
