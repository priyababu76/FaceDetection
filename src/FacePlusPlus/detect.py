import requests
import base64
from src.utils import *

class FaceDetect(object):

    def __init__(self,url,key,secret):
        self.url = url
        self.key = key
        self.secret = secret

    def gen_data(self,image_type,image,index=0):
        return {image_type : image_encode(image_type,image)}

    def gen_files(self,image_type,image,index=0):
        return {image_type : image_encode(image_type, image)}

    def detect(self,image_type,image):

        data = {
            'api_key' : self.key ,
            'api_secret' : self.secret,
        }
        files = {}

        if image_type == PARAM_TYPE['file']:
            files = {**files,**self.gen_files(image_type,image)}

        elif image_type == PARAM_TYPE['base64']:
            data = {**data, **self.gen_data(image_type,image)}

        elif image_type == PARAM_TYPE['url']:
            pass

        try :
            req = requests.post(self.url, data=data, files=files)
            return req
        except requests.HTTPError as e:
            print (e)
            return None