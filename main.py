import requests
from bs4 import BeautifulSoup
import json
from telebot import TeleBot
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.3.886 Yowser/2.5 Safari/537.36'}

token = ''      # TOKEN FROM TELEGRAM BOT HERE
bot = TeleBot(token)


def get_list_of_coins():
    data = requests.get('https://fapi.coinglass.com/api/fundingRate/v2/home', headers=headers)
    data = json.loads(data.text)
    allcoins = []
    for i in range(len(data['data'])):
        try:
            price = str(data['data'][i]['uMarginList'][0]['rate'])
            coin = [float(price), data['data'][i]['symbol']]
            allcoins.append(coin)
        except KeyError:
            pass
    sortallcoins = sorted(allcoins)
    return sortallcoins


def twelwe_coins(sortedlist):
    lsist = []
    for i in range(0,13):
        lsist.append(element[i][1])
    return lsist


def call(tokenname):
    bot.send_message(#id here#, 'Появился новый токен ' + tokenname)   # CHAT_ID HERE
    print('Успешно отстучал в телеграм: ' + 'Появился новый токен ' + tokenname)


def main(bot):
    firstcoinlist = twelwe_coins(get_list_of_coins())
    time.sleep(900)
    coinlist = twelwe_coins(get_list_of_coins())
    result = list(set(firstcoinlist) ^ set(coinlist))
    if result:
        call(result[0])
        main(bot)
    else:
        print('Не появилось новых токенов.')
        main(bot)


if __name__ == '__main__':
    main(bot)
