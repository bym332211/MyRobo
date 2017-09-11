# -*- coding: utf-8 -*-

from aip import AipSpeech
import pygame
import sys
import time
import os

class tts:
    def __init__(self):
        APP_ID = '10079663'
        API_KEY = 'NlBSqpxME1e6vPNNHNVSNpam'
        SECRET_KEY = 'odvdaj8qlAuqnPUdPWK7iVcVgfcZwLEl'
        # 初始化AipSpeech对象
        self.aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


    def say(self, seq):
        cTime = time.strftime("%Y%m%d%H%M%S")

        mp3 = 'audio_' + cTime + '.mp3'
        result  = self.aipSpeech.synthesis(seq, 'zh', 1,
                                      {'vol':5,
                                       'spd':4,
                                       'pit':2,
                                       'per':3,
                                       })

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open(mp3, 'wb') as f:
                print('create ' + mp3)
                f.write(result)
                # f.close()
                # f.__exit__()
                # f.__del__()

        # mp3obj = mp3play.load(mp3)
        # mp3obj.play()
        # time.sleep(10)
        # mp3obj.stop()

        # pygame.init()
        pygame.mixer.init()
        print("Alert!!")
        print('play ' + mp3)

        pygame.mixer.music.load(mp3)
        pygame.mixer.music.play()

        # while 1:
        #     for event in pygame.event.get():
        #         print(event.type)
        #         if event.type == pygame.QUIT:
        #             sys.exit()
        #
        time.sleep(10)
        pygame.mixer.music.stop()
        # pygame.mixer.quit()
        print('delete ' + mp3)
        # os.remove(mp3)
        # time.sleep(3)

if __name__ == '__main__':
    tts_rb = tts()
    tts_rb.say('hi')