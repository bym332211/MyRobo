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
from asr_adapter import asr as Asr
from recoder_adapter import recoder as Rec

define("port", default=7777, help="run on the given port", type=int)
chat = Chat()
tts = Tts()
asr = Asr()
rec = Rec()
class MainHandler(tornado.web.RequestHandler):

    def get(self):
        content = self.get_argument('chat')
        self.write("Robo say:" + roboSay(content))

class AsrHandler(tornado.web.RequestHandler):

    def get(self):
        rec.start()
        content = asr.read_local()
        self.write("Robo say:" + roboSay(content))

def roboSay(input):
    res_seq = chat.chat(input)
    tts.say(res_seq)
    return res_seq


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/chat", MainHandler),
        (r"/asr", AsrHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()