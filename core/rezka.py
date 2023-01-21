#default modules
import json
import random
from os import system
from time import sleep
from datetime import datetime

#download modules
import requests
from bs4 import BeautifulSoup

#created modules
HEADERS = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
}


DOMEN = "https://rezka.ag/"

# function to get html files from site - rezka.ag
def get_html(url, headers=HEADERS):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        return f"something gone wrong {response.status_code}"

#function to get the content from the site and return it as a list with the content
def receive_response(response):
    soup = BeautifulSoup(response, "html.parser")
    all_kino = soup.find("div", class_="b-content__inline_items").find_all("div", class_="b-content__inline_item")
    
    kino_dict = {}
    for item in all_kino:
        title_name = item.find("div", class_="b-content__inline_item-link").find("a").text
        title_url = item.find("div", class_="b-content__inline_item-link").find("a").get("href")
        title_photo = item.find("div", class_="b-content__inline_item-cover").find("a").find("img").get("src")
        title_description = item.find("div", class_="b-content__inline_item-link").find("div").text
        title_description = str(title_description).replace("...,", "")
        kino_dict[title_name] = {
            'url': title_url,
            'photo': title_photo,
            'description': title_description,
        }
    
    return kino_dict


def rezka_parser():
    count_page = 3
    kino = []
    
    for i in range(1, 4):
        URL = f"https://rezka.ag/new/page/{i}"
        response = get_html(url=URL)
        soup = receive_response(response)
        kino.append(soup)
        
    with open("core/json/rezka.json", "w", encoding="UTF-8") as file:
        json.dump(kino, file, indent=4, ensure_ascii=False)

#rezka_parser()

