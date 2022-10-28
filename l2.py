from turtle import width
import cv2
import pickle
import numpy as np

frameWidth = 640
frameHeight = 480
def mc(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
width = 300
height = 500
img = cv2.imread("fin.jpg")
imr = cv2.resize(img,(500,500))
cap = cv2.VideoCapture("vis.mp4")
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
poslist = []
count = 0
while True:
    success,im= cap.read()
    vir = cv2.resize(im,(500,500))
    for pos in poslist:
        cv2.rectangle(imr,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)

    cv2.rectangle(imr,(200,500),(110,230),(255,255,0),2)
    cv2.imshow("imr",imr)
    cv2.setMouseCallback("imr",mc)
    if cv2.waitKey(10) == 500:
        break
    count +=1