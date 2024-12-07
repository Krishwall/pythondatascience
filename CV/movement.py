import numpy as np
import cv2 as cv
cap=cv.VideoCapture(r'CV\movingpeople.mp4')
fgbg=cv.createBackgroundSubtractorKNN(detectShadows=True) # or #fgbg=cv.createBackgroundSubtractorMOG2(detectShadows=True)
while True:

    ret,frame=cap.read()
    if frame is None:
        break
    fgmask= fgbg.apply(frame)

    cv.imshow('Frame',frame)
    cv.imshow('FG MASK FRAME', fgmask)
    

    keyboard= cv.waitKey(30)

    if keyboard=='32':
        break

cap.release()
cap.destroyAllWindows()
