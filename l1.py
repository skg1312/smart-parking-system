from itertools import count
import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
numplateCascade = cv2.CascadeClassifier("cnp.xml")
minarea = 500
color = (0,0,255)
count = 0
cap = cv2.VideoCapture("vis.mp4")
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
while True:
    success,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numplat = numplateCascade.detectMultiScale(imgGray,1.1,4)
    for(x,y,w,h) in numplat:
        area = w*h
        if area > minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
            cv2.putText(img,"number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,1)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("Roi",imgRoi)
    cv2.imshow("Results",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("scan"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,0,255),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,0),1)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1
        