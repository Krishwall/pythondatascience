import matplotlib.pylab as plt
import cv2
import numpy as np

image =cv2.imread("D:\Python Projects\Road.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(image.shape)
height=image.shape[0]
width=image.shape[1]

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
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),) # 5 is the thickness of the line

    img=cv2.addWeighted(img,0.8,blank_image,1,0.0) # overlaps 1 image on top of another 0.8  is the transparency of the image
    return img


region_of_interest_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]

gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

canny_image=cv2.Canny(gray_image,100,200)
cropped_image=region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

lines=cv2.HoughLinesP(cropped_image,
                      rho=2,
                      theta=np.pi/60,
                      threshold=160,
                      lines=np.array([]),
                      minLineLength=40,
                      maxLineGap=20)

image_with_lines=draw_lines(image,lines)
print(lines)
plt.imshow(image_with_lines)
plt.imshow(canny_image)

plt.show()