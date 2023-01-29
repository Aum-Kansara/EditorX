import cv2

def detectFaces(imgPath):
    faceCascade=cv2.CascadeClassifier("static/res/haarcascade_frontalface_default.xml") 
    img=cv2.imread(imgPath)
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=faceCascade.detectMultiScale(imgGray,1.1,4)
    print(faces)
    if faces==():
        return 0
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imwrite(imgPath,img)
    return 1
