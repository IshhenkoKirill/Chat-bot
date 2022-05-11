import telebot
import requests
from decouple import config


bot = telebot.TeleBot(config('BOT'))

class Exchange:
    def __init__(self):
        self.__API_KEY = config('API')
        self.__URL = config('URL')

    def cryptoRequestDirt(self):
      self.__query_params = dict(access_key=self.__API_KEY)
      self.__responce = requests.get(self.__URL, params = self.__query_params)
      self.__dict_dirt = self.__responce.json()
      #Получаем данные в формате JSON и помещаем их в переменную dict_dirt
      self.__dict_clear = self.__dict_dirt['rates']
      #Из соваря dict_dirt извлекаем данные по ключу rates.
      #Значение этого ключа - словарь с котировками
      return self.__dict_clear.keys()
      #Возвращаем список ключей
    def cryptoRequestClear(self):
      self.__query_params = dict(access_key=self.__API_KEY)
      self.__responce = requests.get(self.__URL, params = self.__query_params)
      self.__dict_dirt = self.__responce.json()
      self.__dict_clear = self.__dict_dirt['rates']
      return self.__dict_clear
      #второй метод отличается от первого возвращаемым значением. Здесь это словарь с котировками

dict_crypto = Exchange()

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет \nЯ помогу тебе узнать курсы киптовалют \nОтправь мне /list, чтобы увидеть список криптовалют', parse_mode = None)

@bot.message_handler(commands = ['list'])
def lis(message):
    bot.send_message(message.chat.id, 'Вот список криптовалют', parse_mode = None)
    a = list(dict_crypto.cryptoRequestDirt())
    bot.send_message(message.chat.id, ", ".join(a), parse_mode = None)
    bot.send_message(message.chat.id, 'Напиши в чат, курс какой валюты хочешь узнать', parse_mode = None)

@bot.message_handler(content_types = ['text'])
def txt(message):
    base = dict_crypto.cryptoRequestClear()
    try:
        bot.send_message(message.chat.id, f"Курс {message.text}/USD {base[message.text[:7]]}", parse_mode = None)
    except KeyError:
        bot.send_message(message.chat.id, 'Я не понимаю, проверьте регистр и язык (должен быть английский)', parse_mode = None)


bot.polling(none_stop = True)