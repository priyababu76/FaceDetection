import requests
import base64
from src.utils import *

class FaceCompare(object):
    def __init__(self, url, key, secret):
        self.url = url
        self.key = key
        self.secret = secret

    def gen_data(self, image_type, image, index=0):
        params = image_type

        if index:
            if image_type == PARAM_TYPE['base64']:
                params = params + '_'
            params = params + str(index)
        return {params: image_encode(image_type, image)}

    def gen_files(self, image_type, image, index=0):
        params = image_type

        if index:
            params = params + str(index)
        return {params: image_encode(image_type, image)}

    def compare(self,image_type,image):
        data = {
            'api_key' : self.key ,
            'api_secret' : self.secret,
        }
        files = {}

        size = len(image_type)

        for index in range(size):
            if image_type[index] == PARAM_TYPE['token']:
                pass

            elif image_type[index] == PARAM_TYPE['url']:
                pass

            elif image_type[index] == PARAM_TYPE['file']:
                files = {**files, **self.gen_files(image_type[index], image[index],index+1)}

            elif image_type[index] == PARAM_TYPE['base64']:
                data = {**data, **self.gen_data(image_type[index], image[index],index+1)}

        try :
            req = requests.post(self.url, data=data, files=files)
            return req
        except requests.HTTPError as e:
            print (e)
            return None
