from itertools import count
import cv2
import pickle
try:
    with open('cp','rb') as f:
        pl=pickle.load(f)
except:
    pl =[]
def mc(events,x,y,flags,para):
    if events == cv2.EVENT_LBUTTONDOWN:
        pl.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(pl):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                pl.pop(i)
    with open('cp','wb') as f:
        pickle.dump(pl,f)
width , height = 45,180
while True:
    img = cv2.imread("fin.jpg")
    imr = cv2.resize(img,(500,500))
    for pos in pl:
        cv2.rectangle(imr,pos,(pos[0]+width,pos[1]+height),(0,255,0),2)
    cv2.imshow("imr",imr)
    cv2.setMouseCallback("imr",mc)
    cv2.waitKey(0)