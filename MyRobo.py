# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2009 Facebook
#

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
from adapter.music_adapter import music as Music

define("port", default=7777, help="run on the given port", type=int)
chat = Chat()
tts = Tts()
asr = Asr()

cmd = Cmd()
music = Music()
# listener = Listener()
currentMusicIdx = 0
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        content = self.get_argument('chat')
        res = getResponse(content)
        self.write("Robo say:" + res)

class AsrHandler(tornado.web.RequestHandler):
    def get(self):
        rec = Rec()
        rec.start()
        content = asr.read_local()
        res = getResponse(content)
        self.write("Robo say:" + res)

def getResponse(content):
    res = doCmd(content)
    if not res:
        res = roboSay(content)
    return res

def doCmd(input):
    global currentMusicIdx
    cmd.getCmd(input)
    if cmd.cmds_base == 'common':
        pass
    elif cmd.cmd_type == 'music':
        if cmd.detail_cmd == 'play':
            return playMusic()
        elif cmd.detail_cmd == 'next':
            currentMusicIdx = currentMusicIdx + 1
            return playMusic()
        elif cmd.detail_cmd == 'prev':
            currentMusicIdx = currentMusicIdx - 1
            return playMusic()
        elif cmd.detail_cmd == 'stop' or cmd.detail_cmd == 'pause':
            return 'stop'
        elif cmd.detail_cmd == 'continue':
            playMusic()
    elif cmd.cmds_base == 'other':
        pass

def playMusic():
    global currentMusicIdx
    micId, currentMusicIdx = music.getMusic(currentMusicIdx)
    print(micId)
    return "<iframe frameborder='no' display='none' border='0' marginwidth='0' marginheight='0' width=330 height=86 src='//music.163.com/outchain/player?type=2&id=" + micId + "&auto=1&height=66'></iframe>"


def roboSay(input):
    res_seq = chat.chat(input)
    tts.say(res_seq)
    return res_seq
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
    application = tornado.web.Application([
        (r"/chat", MainHandler),
        (r"/asr", AsrHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()