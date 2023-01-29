import cv2
import numpy as np

# Reading the Image
def sharp_img(imgPath):
    img=cv2.imread('static/imgs/noisy.jpg')

    gaussian_blur=cv2.GaussianBlur(img,(7,7),2)

    # sharpned1=cv2.addWeighted(img,1.5,gaussian_blur,-0.5,0)
    sharpned2=cv2.addWeighted(img,7.5,gaussian_blur,-6.5,0)
    sharpned3=cv2.addWeighted(img,1.5,gaussian_blur,-2.5,0)

    cv2.imwrite(imgPath,img)
    return imgPath
