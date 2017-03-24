# coding=utf-8

import requests

import tornado.web

pageSize = 11
SEARCH_API_ADDR_OF_CLOUD_MUSIC = "http://music.163.com/api/search/pc"


class SearchHandler(tornado.web.RequestHandler):
    
    def get(self):
        type = int(self.get_argument("type"))
        s = self.get_argument("s")
        pageNum = int(self.get_argument("pageNum"))
        offset = (pageNum - 1) * pageSize
        payloads = {
            "offset": offset,
            "limit": pageSize,
            "s": s,
            "type": type
        }
        res = requests.post(SEARCH_API_ADDR_OF_CLOUD_MUSIC, params=payloads)
        self.write(res.content)
