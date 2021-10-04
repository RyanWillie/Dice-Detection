import numpy as np
import cv2

image = cv2.imread("dice.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
th, threshed = cv2.threshold(gray_image, 100, 255, cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
cnts = cv2.findContours(cv2.morphologyEx(threshed, cv2.MORPH_OPEN, np.ones((2,2))), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
nh, nw = image.shape[:2]
for cnt in cnts:
    x,y,w,h = bbox = cv2.boundingRect(cnt)
    if h >= 0.3 * nh:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 0), 10, cv2.LINE_AA)
cv2.imshow("dst", image)
# When everything done, release the capture
cv2.waitKey(0)
cv2.destroyAllWindows()