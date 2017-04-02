# coding = utf-8

import requests

from bs4 import BeautifulSoup

CLOUDMUSIC_SONG_API_ADDR = 'http://music.163.com/api/song/detail?ids={}'


def get_doc_in_get(url):
    return requests.get(url=url).content


def get_soup_by_doc(doc):
    return BeautifulSoup(doc)


def get_songs_info_by_ids(ids):
    return requests.get(CLOUDMUSIC_SONG_API_ADDR.format(ids)).json()
