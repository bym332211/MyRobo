# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import threading

from adapter.asr_adapter import asr as Asr
from tornado.options import define, options
from adapter.chat_adapter import chat as Chat
from adapter.recoder_adapter import recoder as Rec
from adapter.tts_adapter import tts as Tts
from adapter.commonds_adapter import cmdLoader as Cmd

from player.music_player import music_player as mplayer

define("port", default=7778, help="run on the given port", type=int)
chat = Chat()
tts = Tts()
asr = Asr()

cmd = Cmd()
# music = Music()
# currentMusicIdx = 0
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        content = self.get_argument('content')
        res = getResponse(content)
        self.write("Robo say:" + res)

class AsrHandler(tornado.web.RequestHandler):
    def get(self):
        rec = Rec()
        rec.start()
        content = asr.read_local()
        res = getResponse(content)
        self.write("Robo say:" + res)

    def post(self):
        rec = Rec()
        rec.start()
        content = asr.read_local()
        res, mp3 = getResponse(content, "server")
        respon = {'res': res, 'mp3': mp3}
        self.write(respon)

class WebHandler(tornado.web.RequestHandler):
    def get(self):
        # content = "hello"
        # res, mp3 = getResponse(content)
        self.render('./web/test.html', seq="", res="System start", mp3="")

class AjaxHandler(tornado.web.RequestHandler):
    def post(self):
        type = self.get_argument('type')
        if type == "web":
            playMode = self.get_argument('playMode')
            content = self.get_argument('content')
            res, mp3 = getResponse(content, playMode)
            if playMode == "server":
                respon = {'res': res}
            else :
                respon = {'res': res, 'mp3': mp3}
        elif type == "asr":
            rec = Rec()
            rec.start()
            content = asr.read_local()
            res, mp3 = getResponse(content, "server")
            respon = {'res': res, 'content':content, 'mp3': mp3}
            # self.write(respon)
        self.write(respon)

def getResponse(content, playMode = "web"):
    res = doCmd(content)
    if not res:
        res, mp3 = roboSay(content, playMode)
    return res, mp3

def doCmd(input):
    # global currentMusicIdx
    cmd.getCmd(input)
    if cmd.cmds_base == 'common':
        pass
    elif cmd.cmd_type == 'music':
        player = mplayer();
        player.ctlCenter(cmd.detail_cmd)
    elif cmd.cmd_type == 'video':
        pass
    elif cmd.cmds_base == 'other':
        pass



def roboSay(input, playMode = "web"):
    res_seq = chat.chat(input)
    tts.say(res_seq, playMode)
    mp3 = tts.latestMp3.replace('./web/static', 'static')
    return res_seq, mp3
#
# class abc:
#
#     def listening(self):
#         listener.start()
#
#     def start(self):
#         t = threading.Thread(target=self.listening())
#         t.start()

def main():
    # a = abc()
    # a.start()
    tornado.options.parse_command_line()
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "web/static")
    }  # 配置静态文件路径
    application = tornado.web.Application([
        (r"/chat", MainHandler),
        (r"/asr", AsrHandler),
        (r"/web", WebHandler),
        (r"/ajax", AjaxHandler),
    ], **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    print(options.port)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()