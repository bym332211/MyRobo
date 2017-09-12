# 引入Speech SDK
from aip import AipSpeech
import pygame
import time
import wave

#tex	String	合成的文本，使用UTF-8编码，请注意文本长度必须小于1024字节	是
#lang	String	语言选择,填写zh	是
#ctp	String	客户端类型选择，web端填写1	是
#cuid	String	用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内	否
#spd	String	语速，取值0-9，默认为5中语速	否
#pit	String	音调，取值0-9，默认为5中语调	否
#vol	String	语速，取值0-15，默认为5中语速	否
#per	String	发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女	否
# 定义常量
APP_ID = '10079663'
API_KEY = 'NlBSqpxME1e6vPNNHNVSNpam'
SECRET_KEY = 'odvdaj8qlAuqnPUdPWK7iVcVgfcZwLEl '


def robo_say(someword):
    # 初始化AipSpeech对象
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = aipSpeech.synthesis(someword, 'zh', 1, {
        'vol': 5, 'per': 0, 'pit': 1, 'spd': 3
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
    pygame.mixer.init()
    pygame.mixer.music.load('./auido.mp3')

    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()

# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        rs = fp.read()
        return rs

# localfile = ['8k.amr', 'amr']
localfile = ['auido.wav', 'wav']
# 识别本地文件
rtn = aipSpeech.asr(get_file_content(localfile[0]), localfile[1], 8000, {
    'lan': 'zh',
})
#
# # 从URL获取文件识别
# aipSpeech.asr('', 'pcm', 16000, {
#     'url': 'http://121.40.195.233/res/16k_test.pcm',
#     'callback': 'http://xxx.com/receive',
# })
print(str(rtn))
sayword = ''
if rtn['err_no'] == 0:
    sayword = rtn['result']
else :
    sayword = '听不懂你在说什么,我又不是真的人，别要求太高'

robo_say(sayword)





