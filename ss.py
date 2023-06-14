# import cv2
# # import imutils
# # from imutils.perspective import four_point_transform
# import cv2
# # import scipy
# import numpy as np
# # from google.colab.patches import cv2_imshow
import cv2
from matplotlib import pyplot as pit
import numpy as np
# import imutils
import cv2
import os


cam=cv2.VideoCapture(1)
cv2.namedWindow("Pythom webcam Screen App")
img_counter=0
WIDTH = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
HEIGHT = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

while True:
    ret,fram=cam.read()
    bbox_size = (200, 40)
    bbox = [(int(WIDTH // 2 - bbox_size[0] // 2), int(HEIGHT // 2 - bbox_size[1] // 2)),
            (int(WIDTH // 2 + bbox_size[0] // 2), int(HEIGHT // 2 + bbox_size[1] // 2))]

    if not ret:
        print("Faliled to grab frame")
    cv2.rectangle(fram,bbox[0],bbox[1],(0,255,0),3)
    cv2.imshow("test",fram)

    k=cv2.waitKey(1)

    if k%256==27:
        print("Escape hit,closing the app")
        break
    elif k%256==32:
        img_name="opencv_fram_{}.png".format(img_counter)
        cv2.imwrite(img_name,fram)
        image=cv.imread(img_name,cv2.IMREAD_GRAYSCALE )
        imagePath=os.path.join("C:\\Users\\sahil\\OneDrive\\Desktop\\EDI\\Images", img_name)
        cv2.imwrite(imagePath,image)
        print("screenshot taken")
        img_counter+=1
cam.release()
# cam.destroyAllWindows()



image= cv2.imread("C:\\Users\\sahil\\OneDrive\\Desktop\\EDI\\Images\\opencv_fram_0.png")



height, width= image.shape[:2]


image_gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("image_gray",cv2.cvtColor(image_gray,cv2.COLOR_BGR2RGB) )
# cv2.waitKey(0)


ROI= np.array([[(12,height),(12,3),(750,0),(750,height)]], dtype= np.int32)


blank= np.zeros_like(image_gray)


region_of_interest= cv2.fillPoly(blank, ROI,255)

region_of_interest_image= cv2.bitwise_and(image_gray, region_of_interest)

color=(0,0,255)
thickness=10
start_point=(220,220)
end_point=(410,260)
image=cv2.rectangle(region_of_interest_image,start_point,end_point,color,thickness)

bfilter=cv2.bilateralFilter(image, 11, 17, 17)

edged=cv2.Canny(bfilter,30,200)
# cv2.imshow("edged",cv2.cvtColor(edged,cv2.COLOR_BGR2RGB))
# cv2.waitKey(0)
keypoints=cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours=imutils.grab_contours(keypoints)
contours=sorted(contours, key=cv2.contourArea, reverse=True)[ :10]
location=None
for contour in contours:
  approx=cv2.approxPolyDP(contour, 10, True)
  if len(approx)==4:
    location=approx
    break
location
mask=np.zeros(image_gray.shape, np.uint8)
new_image=cv2.drawContours(mask, [location], 0,255, -1)
new_image=cv2.bitwise_and(image,image,mask=mask)
# cv2.imshow("new_image",cv2.cvtColor(new_image,cv2.COLOR_BGR2RGB))
# cv2.waitKey(0)
(x,y)=np.where(mask==255)
(x1,y1)=(np.min(x), np.min(y))
(x2,y2)=(np.max(x), np.max(y))
cropped_image=image_gray[x1:x2+1, y1:y2+1]

cv2.imshow("cropped_image",cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB))
cv2.waitKey(0)

img_name="opencv_fram_{}.png".format(img_counter)
# cv2.imwrite(img_name,cropped_image)
image=cv.imread(img_name,cv2.IMREAD_COLOR )
imagePath=os.path.join("C:\\Users\\sahil\\OneDrive\\Desktop\\EDI\\newImages", img_name)
cv2.imwrite(imagePath,cropped_image)
print("screenshot taken")
img_counter+=1

import cv2
import pytesseract
b=0
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe" #To connect pytesseract to tesseract-wich is pretrained library for OCR 

img2 = cv2.imread('C:\\Users\\sahil\\OneDrive\\Desktop\\EDI\\newImages\\opencv_fram_1.png')
h2Img , w2Img, _ = img2.shape #Gives height of an image relative to window another value which we store in _ variable
box2 = pytesseract.image_to_boxes(img2)
data2 = pytesseract.image_to_data(img2)
for z,a in enumerate(data2.splitlines()):
    # print(z)
    if z!= 0:
        a = a.split()
        # print(a)
        if len(a) == 12: #To get array list with more than 12 array items in that list
            x , y = int(a[6]) , int(a[7]) #data array is slightly bigger so we add 5 in each data array index
            w , h = int(a[8]) , int(a[9])    
            cv2.rectangle(img2 ,(x,y),(x+w,y+h),(255, 0, 0),1)
            #In 3rd argument if we don't add x,y to w,h then  box with different sizes are printed 
            cv2.putText(img2 , a[11],(x, y + 30 ) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,255,0) , 2)
            b=a[11]
            # speak(a[11])
            #we need whole word which is stored at 11 index in array 


print(b)
# cv2.imshow('Image_2',img2)
# cv2.waitKey(0)