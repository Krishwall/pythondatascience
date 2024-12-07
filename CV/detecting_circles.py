import numpy as np
import cv2 as cv

img= cv.imread(r"CV\shapes-709x1024.jpg")
output=img.copy()
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=cv.medianBlur(gray,5)

circles=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,
                        param1=90,param2=75,minRadius=0,maxRadius=0)

detected_circles=np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0,:]:
    cv.circle(output,(x,y),r,(255,0,0),3)# x,y,r are the center and radius of the circle
    # cv.circle(output,(x,y),2,(0,255,255),3) # center of the circle

cv.imshow("output",output)
cv.waitKey(0)
cv.destroyAllWindows()