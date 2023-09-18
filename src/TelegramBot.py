import telebot
from .UserDialog import UserDialog


def create_bot(BOT_TOKEN: str, user_dialog: UserDialog) -> telebot.TeleBot:
    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    def start_bot(message):
        bot.reply_to(message, "Напишите ваше сообщение...")

    @bot.message_handler(func=lambda msg: True)
    def wait_for_reply(message):
        bot.send_message(message.chat.id, "Ожидайте ответа...")

    @bot.message_handler(func=lambda msg: True)
    def reply_to_message(message):
        reply = user_dialog.reply_to_message(message.chat.text)
        bot.send_message(message.chat.id, reply)

    print("Bot is created")
    return bot
