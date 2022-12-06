import telebot

TOKEN = 'AAHyfVtY6_5uH2hfBZemZc3_M2uuOJesD_k'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, "hello")
bot.polling()