import telebot


def create_bot(BOT_TOKEN: str) -> telebot.TeleBot:
    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    def start_bot(message):
        bot.reply_to(message, "Напишите ваше сообщение...")

    @bot.message_handler(func=lambda msg: True)
    def wait_for_reply(message):
        reply = ...
        bot.send_message(message.chat.id, "Ожидайте ответа...")

    return bot
