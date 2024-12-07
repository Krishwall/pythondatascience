import cv2

video=cv2.VideoCapture(r"D:\Python Projects\Sudoku\SampleVideo_1280x720_20mb.mp4")
while True:
    status,frame=video.read()
    # print(status,frame)
    if not status:
        break

    cv2.imshow("video frame",frame)
    if cv2.waitKey(100)==32:
        break

video.release()
cv2.destroyAllWindows()