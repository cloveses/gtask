import hashlib
import time
import json
import calendar
import datetime
import tornado.web
from tweb.web import BaseHandler, route
from models import datamgr

def make_pw(psw, salt=''):
    psw = ''.join((psw,salt))
    psw = psw.encode()
    try:
        ret = hashlib.sha3_512(psw).hexdigest()
    except:
        ret = hashlib.sha512(psw).hexdigest()
        
    return ret

# def make_token(s):
#     curr_time = ''.join((str(time.time()),time.ctime(),
#         time.asctime(),str(time.clock())))
#     md5_str = make_pw(s,curr_time)
#     sha1_str = hashlib.sha1(','.join((s,curr_time)).encode()).hexdigest()
#     return make_pw(md5_str,sha1_str)

def make_token(s):
    return make_pw(s,salt='')


@route('/')
class IndexHdl(BaseHandler):

    def get(self):
        self.write_json({"hint_info":'self.hint_info'})

# @route('/api/upload')
# class UploHdl(BaseHandler):
#     def post(self):
#         # import binascii
#         # data = self.get_argument('data')
#         # print(type(data))
#         # with open('a.jpg','wb') as f:
#         #     f.write(binascii.unhexlify(data.encode('ascii')))
#         import base64
#         data = self.get_argument('data')
#         print(type(data))
#         with open('a.jpg','wb') as f:
#             f.write(base64.b64decode(data.encode('ascii')))
#         self.write_json({'status':0})


# @route('/api/get_img')
# class GetPortraitHdl(BaseHandler):
#     def post(self):
#         keys = ('uid',)
#         params = self.get_params(keys)
#         if params and params['uid'].isdigit():
#             res = datamgr.get_portrait(params['uid'])
#             if res:
#                 self.set_header("Content-Type", "image/jpeg")
#                 self.write(res)
#         else:
#             self.write_json({'status':1})
