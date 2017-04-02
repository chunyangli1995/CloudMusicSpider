# coding=utf-8

import tornado.ioloop

from handlers.search import SearchHandler
from handlers.user import UserHandler


def start_server():
    return tornado.web.Application([
        (r"/search", SearchHandler),
        (r"/user/(\w*)", UserHandler)
    ])


if __name__ == "__main__":
    app = start_server()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
