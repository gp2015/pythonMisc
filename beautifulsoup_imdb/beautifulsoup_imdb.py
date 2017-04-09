from bs4 import BeautifulSoup


import requests
import os


os.environ["BASE_URI"] = "http://www.imdb.com/movies-in-theaters/"


'''
BS DOCS
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''


def bs_imdb():
    response = requests.get(os.environ["BASE_URI"])
    response_text = response.text
    soup = BeautifulSoup(response_text, "html.parser")
    tags = soup.find_all('h4')
    titles = []

    for tag in tags:
        titles.append(tag.get_text())

    for title in titles:
        print(title)


def main():
    bs_imdb()


main()
