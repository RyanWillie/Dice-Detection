import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    edges = cv2.Canny(frame,100,250)

    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(edges, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.imshow("Bounding Boxes",edges)

    cv2.imshow('frame', frame)
    cv2.imshow('Edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()