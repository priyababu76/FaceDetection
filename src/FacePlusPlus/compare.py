import urllib
import urllib.request

from src.utils import *

class FaceCompare(object):

    def __init__(self,url,key,secret,boundary):
        self.url = url
        self.api_key = key
        self.api_secret = secret
        self.boundary = boundary


    def http_append_image(self,image_type,image,index=None):
        data = []

        # todo

        if image_type.find(PARAM_TYPE['url']) != -1:
            pass

        elif image_type.find(PARAM_TYPE['file']) != -1:
            param = image_type + str(index)
            data.append(string2byte('--%s' % self.boundary))
            data.append(string2byte('Content-Disposition: form-data; name="%s"; filename=" "' %
                                    param))
            data.append(string2byte('Content-Type: %s\r\n' %
                                    'application/octet-stream'))
            data.append(image_encode(image_type, image))
            return data

        elif image_type.find(PARAM_TYPE['base64']) != -1 :
            param = type + '_' + str(index)
            return data

        elif image_type.find(PARAM_TYPE['token']) != -1:
            pass



    def http_body(self,image_type,image):
        data = []
        # add api_key
        data.append(string2byte('--%s' % self.boundary))
        data.append(string2byte(
            'Content-Disposition: form-data; name="%s"\r\n' % 'api_key'))
        data.append(string2byte(self.api_key))

        # add api_secret
        data.append(string2byte('--%s' % self.boundary))
        data.append(string2byte(
            'Content-Disposition: form-data; name="%s"\r\n' % 'api_secret'))
        data.append(string2byte(self.api_secret))

        size = len(image_type)
        for index in range(size):
            data = data + self.http_append_image(image_type[index],image[index],index+1)

        data.append(string2byte('--%s--\r\n' % self.boundary))

        return b'\r\n'.join(data)


    def compare(self,image_type,image):
        qrcont = None
        req = urllib.request.Request(self.url)

        req.add_header(
            'Content-Type', 'multipart/form-data; boundary=%s' % self.boundary)

        data = self.http_body(image_type,image)

        try:
            resp = urllib.request.urlopen(req,data=data,timeout=5)
            qrcont = resp.read().decode()
            print (qrcont)
        except urllib.error.HTTPError as e:
            print (e.read().decode())
        return qrcont
