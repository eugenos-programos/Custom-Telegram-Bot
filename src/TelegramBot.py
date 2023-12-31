import telebot
from .UserDialog import UserDialog


def create_bot(BOT_TOKEN: str, user_dialog: UserDialog) -> telebot.TeleBot:
    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    def start_bot(message):
        user_dialog.clear()
        bot.reply_to(message, "Напишите ваше сообщение...")

    @bot.message_handler(func=lambda msg: True)
    def reply_to_message(message):
        bot.send_message(message.chat.id, "Ожидайте ответа...")
        reply = user_dialog.reply_to_message(message.text)
        bot.send_message(message.chat.id, reply)

    print("Bot is created")
    return bot
