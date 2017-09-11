# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2009 Facebook
#

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from chat_adapter import chat as Chat
from tts_adapter import tts as Tts

define("port", default=8888, help="run on the given port", type=int)
chat = Chat()
tts = Tts()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        content = self.get_argument('chat')

        res_seq = chat.chat(content)

        tts.say(res_seq)
        self.write("Robo say:" + res_seq)


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()