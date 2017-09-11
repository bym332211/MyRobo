# -*- coding: utf-8 -*-

import urllib.request as Request
import urllib.parse as Parse
import json

class chat:
    tulin_key = '88461fdcb25949e198843b4b6c776cec'
    tulin_url = 'http://www.tuling123.com/openapi/api'
    def chat(self, seq):
        data = {'key':self.tulin_key,
                'info':seq,
                'userid':'t1'}
        postdata = Parse.urlencode(data)
        postdata = postdata.encode('utf-8')
        res = Request.urlopen(self.tulin_url, postdata)
        str = res.read().decode('utf-8')
        res_dict = json.loads(str)
        res_content = res_dict['text']
        print(res_content)
        return res_content


if __name__ == '__main__':
    chat_rb = chat()
    chat_rb.chat('hi')