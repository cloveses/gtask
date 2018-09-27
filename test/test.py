from urllib import parse,request
import json
import time,random
import base64,binascii
import hashlib


base_url = 'http://127.0.0.1:8000/api'
tel = '13485842157'
# f = open('er.jpg','rb')
# data = binascii.hexlify(f.read())

post_item = [
    # ('/send_sms',{'telephone':tel}),
    ]

def link(item):
    textmod=item[1]
    textmod = parse.urlencode(textmod).encode(encoding='utf-8')

    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0)',"Content-Type": "application/x-www-form-urlencoded"}
    url=''.join((base_url,item[0]))
    print(url)
    req = request.Request(url=url,data=textmod,headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    ret = json.loads(res.decode(encoding='utf-8'))
    print(ret)

if __name__ == '__main__':
    for p in post_item:
        link(p)
