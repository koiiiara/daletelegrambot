# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import telebot
from telebot import util

dict = {}
with open('outfile.txt', "r") as file:
    for line in file:
        if (line.strip().split(":%"))[0].replace(" ", "") not in dict:
            dict[(line.strip().split(":%"))[0].replace(" ", "")] = []
        dict[(line.strip().split(":%"))[0].replace(" ", "")].append((line.strip().split(":%"))[1])

bot = telebot.TeleBot("1712576683:AAGVuzdyLyHrtsv0JVK2aQsC2MQsZfMVk7c", parse_mode=None)

start_text = open("start.txt", "rb").read()
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, start_text, parse_mode= "Markdown")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    word = message.text.upper()
    if word not in dict:
        bot.send_message(message.from_user.id, "К сожалению такого слова нет с словаре😔")
    elif len(dict[word]) == 1:
        splitted_text = util.split_string(dict[word][0], 3000)
        for text in splitted_text:
            bot.send_message(message.from_user.id, text)
        print(dict[word][0])
    else:
        for i in dict[word]:
            splitted_text = util.split_string(i, 3000)
            for text in splitted_text:
                bot.send_message(message.from_user.id, text)



# bot.send_message(message.from_user.id, message.text)


bot.polling()