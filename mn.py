import cv2
import pickle
import numpy as np
try:
    with open('cp','rb') as f:
        pl=pickle.load(f)
except:
    pl =[]
def check(imgpro):
    spaceCount = 0
    for pos in pl:
        x,y = pos
        im = imgpro[y:y+height,x:x+width]
        count = cv2.countNonZero(im)
        if count < 900:
            spaceCount +=1
            color = (0,255,0) 
            tickness = 5
        else:
            color = (0,0,255)
            tickness = 2
        cv2.rectangle(vir,pos,(x+width,y+height),color,tickness)
    cv2.rectangle(vir,(45,30),(250,75),(180,0,180),-1)
    cv2.putText(vir,f'Free:{spaceCount}/{len(pl)}',(50,60),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,255),2)
width , height = 45,180
cap = cv2.VideoCapture("vi0.mp4")
while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0) 
    success ,img = cap.read()
    vir = cv2.resize(img,(500,500))
    imGy = cv2.cvtColor(vir,cv2.COLOR_BGR2GRAY)
    imBr = cv2.GaussianBlur(imGy,(3,3),1)
    imgth = cv2.adaptiveThreshold(imBr,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgm = cv2.medianBlur(imgth,5)
    kernel = np.ones((3,3),np.uint8)
    imgd = cv2.dilate(imgm,kernel,iterations=1)
    check(imgd)
    #cv2.imshow("imgy",imGy)
    #cv2.imshow("imbr",imBr)
    #cv2.imshow("imgth",imgth)
    #cv2.imshow("imgm",imgm)
    #cv2.imshow("imgd",imgd)
    cv2.imshow("img",vir)
    cv2.waitKey(10)