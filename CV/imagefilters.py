import cv2

video=cv2.VideoCapture(r"D:\Python Projects\Sudoku\SampleVideo_1280x720_20mb.mp4")
codec=cv2.VideoWriter_fourcc(*"XVID")

output=cv2.VideoWriter("output.avi",codec,20.0,(640,480))
while True:
    status,frame=video.read(5)

    # print(status,frame)
    if not status:
        break

    newframe=frame*2

    bw=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   

    output.write(bw)
    

    cv2.imshow("video frame",frame)
    # cv2.imshow("video frame 2",newframe)
    # cv2.imshow("b/w",bw)
    # cv2.imshow("rgb",rgb)
   
    if cv2.waitKey(10)==32:
        break

output.release()
video.release()
cv2.destroyAllWindows()