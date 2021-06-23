import requests
import bs4
from config import *
from trash import *

class ParserClient:

    def __init__(self) -> None:
        self.session : requests.Session = requests.Session()
        self.session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def getHabr(self, last_title : str) -> tuple:
        response = self.session.get(habr_url)
        html_tree = bs4.BeautifulSoup(response.text, features='lxml')
        offer_elements = html_tree.find_all('div', {'class' : 'task__title'})

        returnable_title = ""
        returnable_array = []

        for i in range(len(offer_elements)):
            offer_element = offer_elements[i]
            offer_title = offer_element['title']
            offer_link = habrExtend(offer_element.find('a')['href'])
            if i == 0:
                returnable_title = offer_title
            if offer_title == last_title:
                break
            for user in user_preferences:
                for word in user_preferences[user]:
                    if word in offer_title.lower():
                        returnable_array.append((user, offer_title, offer_link))
        
        return returnable_title, returnable_array


    def getWorkspace(self) -> list:
        return []

    def getKwork(self) -> list:
        return []