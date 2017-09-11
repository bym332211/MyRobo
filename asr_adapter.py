# -*- coding: utf-8 -*-

from aip import AipSpeech
import pygame
import sys
import time
import PyAudio
import wave
import os

class asr:
    def my_record(self):
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1,
                         rate=framerate, input=True,
                         frames_per_buffer=NUM_SAMPLES)
        my_buf = []
        count = 0
        while count < TIME * 20:  # 控制录音时间
            string_audio_data = stream.read(NUM_SAMPLES)  # 一次性录音采样字节大小
            my_buf.append(string_audio_data)
            count += 1
            print('.')
        save_wave_file('01.wav', my_buf)
        stream.close()

    def save_wave_file(filename, data):
        '''save the date to the wavfile'''
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)  # 声道
        wf.setsampwidth(sampwidth)  # 采样字节 1 or 2
        wf.setframerate(framerate)  # 采样频率 8000 or 16000
        wf.writeframes(b"".join(
            data))  # https://stackoverflow.com/questions/32071536/typeerror-sequence-item-0-expected-str-instance-bytes-found
        wf.close()

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