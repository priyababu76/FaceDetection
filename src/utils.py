import os
import base64
import time

FACE_URL = {
    'detect': 'https://api-cn.faceplusplus.com/facepp/v3/detect',
    'compare': 'https://api-cn.faceplusplus.com/facepp/v3/compare',
}

USER_CONFIG = {
    'api_key': 'bLGUtVb2PPXbRXrxFGQ53lQAL4s9aiV0',
    'api_secret': 'iKuT2RKxOTD3q790hBqwRV2PszW17zti',
    'boundary': '----------%s' % hex(int(time.time() * 1000)),
}

PARAM_TYPE = {
    'url' : 'image_url',
    'file': 'image_file',
    'base64' : 'image_base64',
    'token' : 'face_token',
}

def image_encode(image_type,image):

    # todo
    if image_type == 'image_url':
        return string2byte(image_type)

    elif image_type == 'image_file':
        with open(image,'rb') as fr:
            return fr.read()

    elif image_type == 'image_base64':
        with open(image,'rb') as fr:
            image_data = fr.read()
            base64_data = base64.b64encode(image_data)
            return base64_data

    elif image_type == 'face_token':
        pass