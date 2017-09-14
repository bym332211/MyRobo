# coding=utf-8
import urllib.request as Request
import ssl
import json

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=NlBSqpxME1e6vPNNHNVSNpam&client_secret=odvdaj8qlAuqnPUdPWK7iVcVgfcZwLEl '
request = Request.Request(host)
# request = urllib.r.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = Request.urlopen(request)
content = json.loads(response.read().decode('utf-8'))
token = content['access_token']

uri='https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=Va5yQRHl********LT0vuXV4&client_secret= 0rDSjzQ20XUj5i********PQSzr5pVw2&'