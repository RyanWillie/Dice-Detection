import numpy as np
import cv2

frame = cv2.imread("dice3.jpg")
edges = cv2.Canny(frame,80,230)

imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(edges, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
diceRects = []
i = 0
dice = 0
process = True
for cnt in contours:
    Area = cv2.contourArea(cnt) 
    if (Area > 400):
        x,y,w,h = cv2.boundingRect(cnt)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        #Check if its a duplicate
        for p in range(dice):
            index = diceRects[p]
            rect2 = cv2.minAreaRect(contours[index])
            box2 = cv2.boxPoints(rect2)
            if((box[0][0] == box2[0][0]) & (box[0][1] == box2[0][1])):
                #print("Found a dupe!")
                process = False
                break
            else:
                process = True

        if(process):
            diceRects.append(i)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            dice = dice + 1
    i = i + 1

#Finding Number within Dice
for p in range(dice):
    index = diceRects[p]
    num = 0
    x,y,w,h = cv2.boundingRect(contours[index])
    rect = cv2.minAreaRect(contours[index])
    img = cv2.getRectSubPix(edges, (w,h), (rect[0]))
    img2 = cv2.getRectSubPix(frame, (w,h), (rect[0]))
    ret2, thresh2 = cv2.threshold(img, 127, 255, 0)
    contours2, hierarchy2 = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    for cnt in contours2:
        Area = cv2.contourArea(cnt) 
        if (Area > 10):
            x,y,w,h = cv2.boundingRect(cnt)
            img2 = cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
            num = num + 1
    cv2.imshow('img', img2)
    print("Num on Dice: ", num)
    cv2.waitKey(0)

cv2.imshow('frame', frame)
cv2.imshow('Edges', edges)
# When everything done, release the capture
cv2.waitKey(0)
cv2.destroyAllWindows()