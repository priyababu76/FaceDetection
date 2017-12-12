from FacePlusPlus.detect import FaceDetect
import time
import os
import cv2

face_url = {
    'detect':'https://api-cn.faceplusplus.com/facepp/v3/detect',
    'compare': 'https://api-cn.faceplusplus.com/facepp/v3/compare',
}

usr_config = {
    'api_key': 'bLGUtVb2PPXbRXrxFGQ53lQAL4s9aiV0',
    'api_secret': 'iKuT2RKxOTD3q790hBqwRV2PszW17zti',
    'boundary':'----------%s' % hex(int(time.time() * 1000)),
}

#图片存储路径
filepath = '/Users/aemonwk/git-project/face++/datasets/player.jpeg'

def get_path():
    return os.path.expanduser('~/datasets')

if __name__ == "__main__":
    
    img = cv2.imread(filepath)
    cv2.namedWindow("origin")
    cv2.imshow("origin", img)

    face_detect = FaceDetect(face_url['detect'],
                        usr_config['api_key'],
                        usr_config['api_secret'],
                        usr_config['boundary']
                        )
    qrcont = face_detect.detect(filepath)

    if qrcont == None :
        print ("error")
    else :
        mydict = eval(qrcont)
        faces = mydict["faces"]
        faceNum = len(faces)
        print("识别到了%d个人脸" % (faceNum))

        for i in range(faceNum):
            face_rectangle = faces[i]['face_rectangle']
            width = face_rectangle['width']
            top = face_rectangle['top']
            left = face_rectangle['left']
            height = face_rectangle['height']
            start = (left, top)
            end = (left + width, top + height)
            color = (55, 255, 155)
            thickness = 3
            cv2.rectangle(img, start, end, color, thickness)

        cv2.namedWindow("detect after")
        cv2.imshow("detect after", img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
