import cv2
import numpy as np




def getEdges(imgPath):
    img=cv2.imread(imgPath)
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
    imgCanny=cv2.Canny(imgBlur,50,50)
    imgBlank=np.zeros_like(img)
    cv2.imwrite(imgPath,imgCanny)
    return imgPath