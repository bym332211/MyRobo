# -*- coding: utf-8 -*-

from aip import AipSpeech
import pygame
import sys
import time
import PyAudio
import wave
import os

class asr:


    def __init__(self):
        APP_ID = '10079663'
        API_KEY = 'NlBSqpxME1e6vPNNHNVSNpam'
        SECRET_KEY = 'odvdaj8qlAuqnPUdPWK7iVcVgfcZwLEl'
        # 初始化AipSpeech对象
        self.aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 读取文件
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 识别本地文件
    def read_local(self):
        self.aipSpeech.asr(self.get_file_content('audio.pcm'), 'pcm', 16000, {
        'lan': 'zh',
    })
    # 从URL获取文件识别
    def read_remote(self):
        self.aipSpeech.asr('', 'pcm', 16000, {
        'url': 'http://121.40.195.233/res/16k_test.pcm',
        'callback': 'http://xxx.com/receive',
    })

if __name__ == '__main__':
    tts_rb = tts()
    tts_rb.say('hi')