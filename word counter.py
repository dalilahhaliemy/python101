# say we wanna count words in a webpage

import requests
from bs4 import BeautifulSoup
import operator

# 1. start by getting the links in the list


def start(url):

    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    for post_text in soup.findAll("a", {"class": "l lLrAF"}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)


start("https://www.google.com/search?q=ringgit&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiu5-jS0ubmAhWRT30KHawBCxMQ_AUoAnoECBQQBA&biw=1109&bih=708")

