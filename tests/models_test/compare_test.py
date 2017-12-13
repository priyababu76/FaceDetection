from src.FacePlusPlus.compare import FaceCompare
import time
import os
import cv2

face_url = {
    'detect': 'https://api-cn.faceplusplus.com/facepp/v3/detect',
    'compare': 'https://api-cn.faceplusplus.com/facepp/v3/compare',
}

usr_config = {
    'api_key': 'bLGUtVb2PPXbRXrxFGQ53lQAL4s9aiV0',
    'api_secret': 'iKuT2RKxOTD3q790hBqwRV2PszW17zti',
    'boundary': '----------%s' % hex(int(time.time() * 1000)),
}

# 图片存储路径
imagepath1 = '/Users/aemonwk/git-project/face++/datasets/curry1.jpeg'
imagepath2 = '/Users/aemonwk/git-project/face++/datasets/curry2.jpeg'

if __name__ == "__main__":

    cmp = FaceCompare(
        url = face_url['compare'],
        key = usr_config['api_key'],
        secret = usr_config['api_secret'],
        boundary = usr_config['boundary']
    )

    qrcont = cmp.compare(imagepath1,imagepath2)

    if qrcont == None:
        print ("HTTP error")
    else:
        mydict = eval(qrcont)
        print ("image1跟image2中人脸的置信度为:",mydict['confidence'])