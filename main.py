import telebot
import time
from parser_client import ParserClient
import json
from mailer import Mailer


parser_client = ParserClient();
with open('cash.json', 'r', encoding='utf-8') as file:
    cash = json.loads(file.read())
    habr_last = cash['habr']


while True:
    print('parsing')
    results : list = []
    habr_last, habr_offers = parser_client.getHabr(habr_last)
    cash['habr'] = habr_last
    print(habr_offers)
    results.extend(habr_offers)
    # input()
    results.extend(parser_client.getWorkspace())
    results.extend(parser_client.getKwork())
    
    with open('cash.json', 'w') as file:
        file.write(json.dumps(cash))

    bot = Mailer()
    for result in results:
        bot.mail(result)
    time.sleep(180)