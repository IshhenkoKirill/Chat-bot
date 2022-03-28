import requests
api_key = '8f5695c0ae628374e4fdec9136da0580'
url = 'http://api.coinlayer.com/live'
query_params = dict(access_key=api_key)
responce = requests.get(url, params = query_params)
dict_dirt = responce.json()
#получаем данные в формате JSON и помещаем их в переменную dict_dirt
dic_clear = dict_dirt['rates']
#из соваря dict_dirt извлекаем данные по ключу rates.
#Значение этого ключа - словарь с котировками
print(f"Курс BTC/USD {dic_clear['BTC']}")
print(f"Курс ETH/USD {dic_clear['ETH']}")
print(f"Курс XRP/USD {dic_clear['XRP']}")
#с помощью f-строки исообщаем курс указанных в качестве ключа валют