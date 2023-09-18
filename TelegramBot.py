from dotenv import load_dotenv
import os
import telebot


load_dotenv("settings/key.env")

BOT_TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.reply_to(message, "Напишите ваше сообщение...")


@bot.message_handler(func=lambda msg: True)
def reply_to_message(message):
    reply = ...
    bot.send_message(message.chat.id, "Ожидайте ответа...")


@bot.message_handler(func=lambda msg: True)
def reply_to_message(message):
    reply = ...
    bot.reply_to(message, reply)

bot.infinity_polling()

