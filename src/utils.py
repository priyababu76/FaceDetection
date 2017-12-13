import os

def string2byte(strr):
    return strr.encode()

def encode_image(filepath):
    with open(filepath,'rb') as fr:
        return fr.read()