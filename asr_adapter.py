# -*- coding: utf-8 -*-

from aip import AipSpeech

class asr:


    def __init__(self):
        APP_ID = '10079663'
        API_KEY = 'NlBSqpxME1e6vPNNHNVSNpam'
        SECRET_KEY = 'odvdaj8qlAuqnPUdPWK7iVcVgfcZwLEl'
        # 初始化AipSpeech对象
        self.aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 读取文件
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 识别本地文件
    def read_local(self):
        audio = 'output.wav'
        # audio = './back/8k.amr'
        response = self.aipSpeech.asr(self.get_file_content(audio), 'wav', 16000, {
        # response = self.aipSpeech.asr(self.get_file_content(audio), 'amr', 8000, {
            'lan': 'zh',
        })
        print(response['result'])
        return response['result']
    # # 从URL获取文件识别
    # def read_remote(self):
    #     self.aipSpeech.asr('', 'pcm', 16000, {
    #     'url': 'http://121.40.195.233/res/16k_test.pcm',
    #     'callback': 'http://xxx.com/receive',
    # })

if __name__ == '__main__':
    asr_rb = asr()
    asr_rb.read_local()