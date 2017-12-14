from src.FacePlusPlus.compare import FaceCompare
import os
import cv2
from src.utils import *

# 图片存储路径
image_path1 = '/Users/aemonwk/git-project/face++/datasets/curry1.jpeg'
image_path2 = '/Users/aemonwk/git-project/face++/datasets/curry2.jpeg'

if __name__ == "__main__":

    image_type = [
        PARAM_TYPE['base64'],
        PARAM_TYPE['base64'],
    ]

    image = [
        image_path1,
        image_path2
    ]

    cmp = FaceCompare(
            FACE_URL['compare'],
            USER_CONFIG['api_key'],
            USER_CONFIG['api_secret'],
    )

    resp = cmp.compare(image_type,image)

    if resp == None:
        print("HTTP error")
    else:
        qrcont = resp.text
        print (qrcont)
        mydict = eval(qrcont)
        print ("image1跟image2中人脸的置信度为:",mydict['confidence'])