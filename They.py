import telebot
import requests

bot = telebot.TeleBot('5132380101:AAEIqIrhvGfI8LlTUsdGJ2p28GFnbf8oslY')
#url_telegram = 'https://api.telegram.org/bot'
class Exchange:
    def __init__(self):
        self.__api_key = '8f5695c0ae628374e4fdec9136da0580'
        self.__url = 'http://api.coinlayer.com/live'

    def cryptoRequestDirt(self):
      self.__query_params = dict(access_key=self.__api_key)
      self.__responce = requests.get(self.__url, params = self.__query_params)
      self.__dict_dirt = self.__responce.json()
      #Получаем данные в формате JSON и помещаем их в переменную dict_dirt
      self.__dict_clear = self.__dict_dirt['rates']
      #Из соваря dict_dirt извлекаем данные по ключу rates.
      #Значение этого ключа - словарь с котировками
      return self.__dict_clear.keys()
      #Возвращаем список ключей
    def cryptoRequestClear(self):
      self.__query_params = dict(access_key=self.__api_key)
      self.__responce = requests.get(self.__url, params = self.__query_params)
      self.__dict_dirt = self.__responce.json()
      self.__dict_clear = self.__dict_dirt['rates']
      return self.__dict_clear
      #второй метод отличается от первого возвращаемым значением. Здесь это словарь с котировками

dict_crypto = Exchange()

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я помогу тебе узнать курсы киптовалют. Отправь мне /lis, чтобы увидеть весь список', parse_mode = None)

@bot.message_handler(commands = ['lis'])
def lis(message):
    bot.send_message(message.chat.id, 'Вот список криптовалют', parse_mode = None)
    a = list(dict_crypto.cryptoRequestDirt())
    bot.send_message(message.chat.id, ", ".join(a), parse_mode = None)
    bot.send_message(message.chat.id, 'Курс какой криптовалюты ты хочешь узнать? ', parse_mode = None)

@bot.message_handler(content_types = ['text'])
def text(message):
    base = dict_crypto.cryptoRequestClear()
    bot.send_message(message.chat.id, f"Курс {message.text}/USD {base[message.text[:7]]}", parse_mode = None)


bot.polling(none_stop = True)