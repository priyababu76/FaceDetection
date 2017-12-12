import urllib
import urllib.request

def string2byte(strr):
    return strr.encode()

def encode_image(filepath):
    with open(filepath, 'rb') as fr:
        return fr.read()

class FaceDetect(object):
    
    def __init__(self,url,key,secret,boundary):
        self.url = url
        self.api_key = key
        self.api_secret = secret
        self.boundary = boundary

    def http_body(self,filepath):
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

        # add image bytes
        data.append(string2byte('--%s' % self.boundary))
        data.append(string2byte('Content-Disposition: form-data; name="%s"; filename=" "' %
                                'image_file'))
        data.append(string2byte('Content-Type: %s\r\n' %
                                'application/octet-stream'))
        data.append(encode_image(filepath))
        data.append(string2byte('--%s--\r\n' % self.boundary))

        return '\r\n'.encode().join(data)


    def detect(self,filepath):
        qrcont = None   

        req = urllib.request.Request(self.url)
        req.add_header(
            'Content-Type', 'multipart/form-data; boundary=%s' % self.boundary)
        data = self.http_body(filepath)
        try:
            resp = urllib.request.urlopen(req,data=data,timeout=5)
            qrcont = resp.read()
            print (qrcont)
        except urllib.error.HTTPError as e:
            print (e.read())

        return qrcont

