# coding=utf-8

import time

from selenium import webdriver
import tornado.web

from utils import get_doc_in_get
from utils import get_songs_info_by_ids
from utils import get_soup_by_doc

CLOUDMUSIC_USER_DOMAIN = 'http://music.163.com/user/home?id={}'
CLOUDMUSIC_SONG_RANK_DOMAIN = 'http://music.163.com/user/songs/rank?id={}'
CLOUDMUSIC_DOMAIN = 'http://music.163.com{}'


class UserHandler(tornado.web.RequestHandler):

    def get(self, user_id):
        user_url_in_cloudmusic = CLOUDMUSIC_USER_DOMAIN.format(user_id)
        user_doc = get_doc_in_get(url=user_url_in_cloudmusic)
        user_soup = get_soup_by_doc(doc=user_doc)
        collectlistCount = int(user_soup.find(id='sHeader').h3.span.text[
                           len(user_soup.find(id='sHeader').h3.span.text)-3:-1
        ])
        # simulation action in chrome by selenium webdriver
        browser = webdriver.Chrome()
        browser.get(CLOUDMUSIC_SONG_RANK_DOMAIN.format(user_id))
        time.sleep(3)
        browser.switch_to_frame('g_iframe')
        songsall = get_soup_by_doc(browser.page_source)
        song_ul = songsall.find(id='m-record').find_all('li')
        songs_info = []
        authors_infos = []
        song_ids = []
        for song_li in song_ul:
            song_url = song_li.find('a')['href']
            song_id = song_url[song_url.rindex('=')+1:]
            song_ids.append(int(song_id))
            authors_a = song_li.find_all('div')[1].find('span').span.find_all('a')
            authors_info = [
                            {
                                'author_link': CLOUDMUSIC_DOMAIN.format(author_a['href']),
                                'author_name': author_a.get_text()
                            }
                            for author_a in authors_a
            ]
            authors_infos.append(authors_info)
        songs = get_songs_info_by_ids(ids=song_ids)['songs']
        for authors_info, song in zip(authors_infos, songs):
            songs_info.append({
                        'authors_info': authors_info,
                        'playTime': song['bMusic']['playTime']
                    })
        res = {
            'collectlistCount': collectlistCount,
            'songsall': songs_info
        }
        self.write(res)
        browser.close()
