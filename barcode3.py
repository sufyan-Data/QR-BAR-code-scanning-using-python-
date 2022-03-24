import cv2
from pyzbar.pyzbar import decode
import numpy as np
#img=cv2.imread("websiteQRCode_noFrame.jpg") 
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,640)
while True:

    success,img=cap.read()
    code=decode(img)
    for barcode in decode(img):
        print(barcode.data)
        mydata=barcode.data.decode('utf-8')
        print(mydata)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,0,25),5)
        pts2=barcode.rect
        cv2.putText(img,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_TRIPLEX,
                    0.9,(255,0,0),2)

    cv2.imshow("result",img)
    cv2.waitKey(1)
    


