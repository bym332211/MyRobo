# coding=utf-8
import urllib.request as Request
import ssl
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=NlBSqpxME1e6vPNNHNVSNpam&client_secret=odvdaj8qlAuqnPUdPWK7iVcVgfcZwLEl '
request = Request.Request(host)
# request = urllib.r.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = Request.urlopen(request)
content = response.read()
if (content):
    print(content)