
# Default modules - Модули по умолчанию
import json
import random
from os import system
from time import sleep
from datetime import datetime

# Downloaded libraries - Скаченные библиотеки
import requests
from bs4 import BeautifulSoup

# Created module - Созданный модуль
DOMEN = "http://rezka.ag"

URL = "https://rezka.ag/new/"


HEADERS = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

def get_html(url, headers=HEADERS):
    responce = requests.get(url, headers=headers)
    if responce.status_code == 200:
        return responce.content
    else:
        return f"Что-то пошло не так {responce.status_code}"



def receive_response(responce):
    soup = BeautifulSoup(responce, "lxml")
    all_kino = soup.find("div", class_="b-content__inline").find_all("div", class_="b-content__inline_item")
    
    kino_dict = {}
    for item in all_kino:
        title_name = item.find("div", class_="b-content__inline_item-link").find("a").text
        title_url = item.find("div", class_="b-content__inline_item-link").find("a").get("href")
        title_image = item.find("div", class_="b-content__inline_item-cover").find("a").find("img").get("src")
        title_descrip = item.find("div", class_="b-content__inline_item-link").find("div").text
        title_descrip = str(title_descrip).replace("...,", "")
        kino_dict[title_name] = {
            "url": title_url,
            "photo": title_image,
            "description": title_descrip
        }
    
    return kino_dict




def rezka_parser():
    count_page = 3
    kino = []
    
    for i in range(1, count_page+1):
        URL = f"https://rezka.ag/new/page/{i}/"
        responce = get_html(url=URL)
        soup = receive_response(responce)
        
        kino.append(soup)
        
    with open("core/all_kino.json", "w", encoding="UTF-8") as file:
        json.dump(kino, file, indent=4, ensure_ascii=False)


