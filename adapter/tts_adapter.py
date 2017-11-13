# -*- coding: utf-8 -*-

from aip import AipSpeech
from player.music_player import music_player as mplayer
import time
import os

class tts:
    tmpPath = './web/static/sounds/tmp/'
    latestMp3 = tmpPath + 'audio_20170912091507.mp3'
    def __init__(self):
        APP_ID = '10079663'
        API_KEY = 'NlBSqpxME1e6vPNNHNVSNpam'
        SECRET_KEY = 'odvdaj8qlAuqnPUdPWK7iVcVgfcZwLEl'
        # 初始化AipSpeech对象
        self.aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


    def deleteMp3(self):
        list = os.listdir(self.tmpPath)
        if list.__len__() > 5:
            f = list[0];
            try:
                print('delete latestMp3: ' + self.tmpPath + str(f))
                os.remove(self.tmpPath + str(f))
            except Exception as e:
                print(e)
            # for f in list:
            #     try :
            #         print('delete latestMp3: ' + self.tmpPath + str(f))
            #         os.remove(self.tmpPath + str(f))
            #     except Exception as e:
            #         print(e)

    def say(self, seq, playMode = "web"):
        cTime = time.strftime("%Y%m%d%H%M%S")
        self.deleteMp3()
        mp3 = self.tmpPath + 'audio_' + cTime + '.mp3'
        result  = self.aipSpeech.synthesis(seq, 'zh', 1,
                                      {'vol':5,
                                       'spd':4,
                                       'pit':2,
                                       'per':0,
                                       })

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open(mp3, 'wb') as f:
                print('create ' + mp3)
                f.write(result)
        time.sleep(1)
        if playMode == "server":
            player = mplayer()
            player.playLocalMusic(mp3)
        self.latestMp3 = mp3


if __name__ == '__main__':
    tts_rb = tts()
    tts_rb.say('hi')