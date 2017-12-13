import urllib
import urllib.request

from src.utils import *

class FaceCompare(object):
    def __init__(self,url,key,secret,boundary):
        self.url = url
        self.api_key = key
        self.api_secret = secret
        self.boundary = boundary

    def http_body(self,imagepath1,imagepath2):
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

        # add image1 bytes
        data.append(string2byte('--%s' % self.boundary))
        data.append(string2byte('Content-Disposition: form-data; name="%s"; filename=" "' %
                                'image_file1'))
        data.append(string2byte('Content-Type: %s\r\n' %
                                'application/octet-stream'))
        data.append(encode_image(imagepath1))

        # add image2 bytes
        data.append(string2byte('--%s' % self.boundary))
        data.append(string2byte('Content-Disposition: form-data; name="%s"; filename=" "' %
                                'image_file2'))
        data.append(string2byte('Content-Type: %s\r\n' %
                                'application/octet-stream'))
        data.append(encode_image(imagepath2))


        data.append(string2byte('--%s--\r\n' % self.boundary))

        return '\r\n'.encode().join(data)


    def compare(self,imagepath1,imagepath2):
        qrcont = None
        req = urllib.request.Request(self.url)

        req.add_header(
            'Content-Type', 'multipart/form-data; boundary=%s' % self.boundary)

        data = self.http_body(imagepath1,imagepath2)

        try:
            resp = urllib.request.urlopen(req,data=data,timeout=5)
            qrcont = resp.read().decode()
            print (qrcont)
        except urllib.error.HTTPError as e:
            print (e.read().decode())
        return qrcont
