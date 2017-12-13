import urllib
import urllib.request

from src.utils import *

class FaceDetect(object):
    
    def __init__(self,url,key,secret,boundary):
        self.url = url
        self.api_key = key
        self.api_secret = secret
        self.boundary = boundary

    def http_append_image(self,image_type,image):

        # todo

        data = []
        if image_type.find(PARAM_TYPE['url']) != -1:
            param = image_type
            data.append(string2byte('--%s' % self.boundary))
            data.append(string2byte('Content-Disposition: form-data; name="%s"; filename=" "' %
                                    param))
            data.append(string2byte('Content-Type: %s\r\n' %
                                    'application/octet-stream'))
            data.append(image_encode(image_type, image))
            return data

        elif image_type.find(PARAM_TYPE['file']) != -1:
            param = image_type
            data.append(string2byte('--%s' % self.boundary))
            data.append(string2byte('Content-Disposition: form-data; name="%s"; filename=" "' %
                                    param))
            data.append(string2byte('Content-Type: %s\r\n' %
                                    'application/octet-stream'))
            data.append(image_encode(image_type, image))
            return data

        elif image_type.find(PARAM_TYPE['base64']) != -1 :
            param = image_type
            data.append(string2byte('--%s' % self.boundary))
            data.append(string2byte('Content-Disposition: form-data; name="%s"; filename=" "' %
                                    param))
            data.append(string2byte('Content-Type: %s\r\n' %
                                    'application/octet-stream'))
            data.append(image_encode(image_type, image))
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

        # detect single image
        data = data + self.http_append_image(image_type[0],image[0])

        data.append(string2byte('--%s--\r\n' % self.boundary))

        return b'\r\n'.join(data)


    def detect(self,image_type,image):
        qrcont = None   

        req = urllib.request.Request(self.url)
        req.add_header(
            'Content-Type', 'multipart/form-data; boundary=%s' % self.boundary)

        # req.add_header(
        #     'Content-Type', 'application/octet-stream; boundary=%s' % self.boundary)

        data = self.http_body(image_type,image)
        try:
            resp = urllib.request.urlopen(req,data=data,timeout=5)
            qrcont = resp.read().decode()
            print (qrcont)
        except urllib.error.HTTPError as e:
            print (e.read())

        return qrcont

