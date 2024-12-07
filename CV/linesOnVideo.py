import matplotlib.pylab as plt
import cv2
import numpy as np

# image =cv2.imread("D:\Python Projects\Road.png")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def region_of_interest(img, vertices):
    mask=np.zeros_like(img)
    # channel_count=img.shape[2] # since we are using a gray scale image
    match_mask_color=255  # channek_count=3 (R G B= (255 ,255 ,255)
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image=cv2.bitwise_and(img, mask)
    return masked_image

def  draw_lines(img,lines):
    copy_img=np.copy(img)
    blank_image=np.zeros((copy_img.shape[0],copy_img.shape[1],3),dtype=np.uint8) # np.zeoros

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),4) # 5 is the thickness of the line

    img=cv2.addWeighted(img,0.8,blank_image,1,0.0) # overlaps 1 image on top of another 0.8  is the transparency of the image
    return img

def process(image):
    
    height=image.shape[0]
    width=image.shape[1]

    region_of_interest_vertices = [
        (0, height),
        (width/2, height*0.7),
        (width, height)
    ]

    gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

    canny_image=cv2.Canny(gray_image,100,120)
    
    cropped_image=region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
    # plt.imshow(cropped_image)
    # plt.show()
    lines=cv2.HoughLinesP(cropped_image,
                        rho=2,
                        theta=np.pi/60,
                        threshold=150,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=200)

    image_with_lines=draw_lines(image,lines)
    return image_with_lines

cap=cv2.VideoCapture(r"CV\newcarvid.mp4")

while (cap.isOpened()):
    ret,frame=cap.read()
    
    frame=process(frame)
    cv2.imshow("frame",frame)
        # plt.imshow(frame)
        # plt.show()
        # break
    if cv2.waitKey(30) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()