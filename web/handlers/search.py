# coding=utf-8

import tornado.web

class SearchHandler(tornado.web.RequestHandler):
    
    def get(self):
        type = self.get_argument("type")
