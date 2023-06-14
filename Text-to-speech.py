import cv2
import pytesseract
import pyttsx3 
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id) # you can change to female voice just by replacing 0 by 1 in voices[0].

img_name = ' '
img_ng = img_name
def speak(audio):
        engine.say(audio)
        engine.runAndWait()

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe" #To connect pytesseract to tesseract-wich is pretrained library for OCR 
#image_to_string method in pytesseract gives all the text which is written inside image

# video = cv2.VideoCapture('https://192.168.43.94:8080/video') 
# #video = cv2.VideoCapture(0)#to connect mobile webcam with pytesseract /video to get only video feed to get captured 
# video.set(3,640) #Set width and height of webcam window
# video.set(4,400) 
# engine = pyttsx3.init()

cam  = cv2.VideoCapture(0)

# cv2.namedWindow("Python_webcam_SS")

img_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print('Failed to grab frame ')
        break

    cv2.imshow("Test",frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
        print("Escape hit")
        break
    elif k%256 == 32:
        img_name="opencv_fram_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        imgpath = os.path.join("D:\\Piyush\\SEM 1\\PycharmProjects\\pythonProject\\images",img_name)
        cv2.imwrite(imgpath,frame)
        print("screenshot taken")
        img_counter+=1

img2 = cv2.imread("D:\\Piyush\\SEM 1\\PycharmProjects\\pythonProject\\images"+"\\"+str(img_name))
cv2.imshow("Image",img2)
cv2.waitKey(0)

#img1 = cv2.imread('D:\Piyush\PycharmProjects\pythonProject\img1.png')
# cam  = cv2.VideoCapture(0)

# cv2.namedWindow("Python_webcam_SS")

# img_counter = 0

# while True:
#     ret, frame = cam.read()

#     if not ret:
#         print('Failed to grab frame ')
#         break

#     cv2.imshow("Test",frame)

#     k = cv2.waitKey(1)

#     if k%256 == 27:
#         print("Escape hit")
#         break

#     elif k%256 == 32:
#         img_name = "opencv_frame_{}.png".format(img_counter)
#         cv2.imwrite(img_name,frame)
#         img_counter+=1


# # cv2.imshow('image 1',img1)
#cv2.imshow('image 2',img2)
# h1Img,w1Img, _ =  img1.shape
h2Img , w2Img, _ = img2.shape #Gives height of an image relative to window another value which we store in _ variable

# #print(h2Img)
#  box1 = pytesseract.image_to_boxes(img1) #which gives  x & y cords along with width and height of each character 
box2 = pytesseract.image_to_boxes(img2)

#print(box2)
#print(box2.splitlines())
# # data1 = pytesseract.image_to_data(img1)
data2 = pytesseract.image_to_data(img2)
#print(data2.splitlines())
# filewrite = open("string.txt","w")
# for z,a in enumerate(data2.splitlines()):
#     if z!= 0:
#         a = a.split()
#         if len(a) == 12:
#             x , y = int(a[6]) , int(a[7]) #data array is slightly bigger so we add 5 in each data array index
#             w , h = int(a[8]) , int(a[9])    
#             cv2.rectangle(img2 ,(x,y),(x+w,y+h),(255, 0, 0),1)
#             #In 3rd argument if we don't add x,y to w,h then  box with different sizes are printed 
#             cv2.putText(img2 , a[11],(x,y + 30 ) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,255,0) , 2)
#             filewrite.write(a[11] + " ")
# filewrite.close()
# fileread = open("string.txt","r")
# lang = 'en'
# line = fileread.read()
# if line != ' ':
#     speech = gTTS(text=line,lang = lang,slow=False)
#     speech.save("test.mp3")

# cv2.imshow('gtts',img2)
# cv2.waitKey(0)
# playsound('D:\\Piyush\\PycharmProjects\\pythonProject\\test.mp3')
# s = ""
# while True: #to continuously pass each frame form video 
#     check , Frame = video.read() # To check if it's receiving a framee or not and if yes then read each individual frame 
#     data3 = pytesseract.image_to_data(Frame) #We are taking each frame from camera and  passing each frame to convert it into data
#     for z,a in enumerate(data3.splitlines()):
#         if z!= 0:
#             a = a.split()
#             if len(a) == 12:
#                 x , y = int(a[6]) , int(a[7]) #data array is slightly bigger so we add 5 in each data array index
#                 w , h = int(a[8]) , int(a[9])    
#                 cv2.rectangle(Frame ,(x,y),(x+w,y+h),(255, 0, 0),1)
#                 #In 3rd argument if we don't add x,y to w,h then  boxes with different sizes are printed 
#                 cv2.putText(Frame , a[11],(x,y + 30 ) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,255,0) , 2)
#                 #s = s +a[11]
#                 speak(a[11])
#                 file = open("writing.txt", "a")
#                 file.write(a[11])
#                 print(file.read())
#                 file.close()
#                 break
#                 #filewrite.write(a[11] + " ")

#     #filewrite.close()
#     fileread = open("string.txt","r")
#     lang = 'en'
#     line = fileread.read()
#     if line != ' ':
#         engine.say(line)
#         engine.runAndWait()


#     cv2.imshow('gtts',img2)
#     cv2.imshow('Video_Capture',Frame)
#     #print(s)
#     #playsound("test1.mp3")
    
#Creating bounding boxes(box around word)
# for z,a in enumerate(data1.splitlines()):
#     if z!= 0:
#         a = a.split()
#         if len(a) == 12:
#             x , y = int(a[6]) , int(a[7]) #data array is slightly bigger so we add 5 in each data array index
#             w , h = int(a[8]) , int(a[9])    
#             cv2.rectangle(img1 ,(x,y),(x+w,y+h),(255, 0, 0),1)
#             #In 3rd argument if we don't add x,y to w,h then  box with different sizes are printed 
#             cv2.putText(img1 , a[11],(x,y + 30 ) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,255,0) , 2)
for z,a in enumerate(data2.splitlines()):
        #print(z)
        if z!= 0:
            a = a.split()
            #print(a)
            if len(a) == 12: #To get array list with more than 12 array items in that list
                x , y = int(a[6]) , int(a[7]) #data array is slightly bigger so we add 5 in each data array index
                w , h = int(a[8]) , int(a[9])    
                cv2.rectangle(img2 ,(x,y),(x+w,y+h),(255, 0, 0),1)
                #In 3rd argument if we don't add x,y to w,h then  box with different sizes are printed 
                cv2.putText(img2 , a[11],(x, y + 30 ) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,255,0) , 2)
                cv2.imshow('Image_2',img2)
                print(a[11])
                speak(a[11])
                #we need whole word which is stored at 11 index in array 

if cv2.waitKey(0) & 0xFF == ord('q'): #If waitkey is more than one second and user hits the 'q' key it will close and end the program 
                cam.release()
                cv2.destroyAllWindows()
                cv2.waitKey(0)
# cv2.imshow('Capture_1' , img1)
# cv2.imshow('Capture_2' , img2)
# cv2.waitKey(0)

# for i in box1.splitlines():
#     i = i.split() #Converts one string of values into list of values and allow us to access them as an array
#     print(i) #['p', '131', '63', '139', '76', '0'] = [Character_which is detected , x-cordinate,y-coordinate ,width , height]
#     x , y = int(i[1]) , int(i[2])
#     w , h = int(i[3]) , int(i[4])

#     cv2.rectangle(img1 ,(x,h1Img - y),(w, h1Img - h),(255, 0, 0),1)#Bounding boxes shows correctly at the char position  
#     cv2.putText(img1 , i[0],(x,h1Img - y + 25 ) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,255,0) , 2)


# for i in box2.splitlines():
#     i = i.split() #Converts one set of values of one character into list of values and allow us to access them as an array
#     #print(i) #['p', '131', '63', '139', '76', '0'] = [text_which is detected , x-cordinate,y-coordinate ,width , height]
#     x , y = int(i[1]) , int(i[2])
#     w , h = int(i[3]) , int(i[4])

#     cv2.rectangle(img2  ,(x,h2Img- y),(w,h2Img - h),(255, 0, 0),1)
#     print(h2Img,y)
#     cv2.putText(img2 , i[0] , (x,h2Img - y + 25) , cv2.FONT_HERSHEY_PLAIN , 1 , (0,255,0) , 2) 
#     #3rd argument we add 25 to y to get printed string somewhat below text
#     #3rd argument will get start at the bottombound

# cv2.imshow('Image_1',img1)

# cv2.waitKey(0)

#print(pytesseract.image_to_string(img1)) #Gives us string of multiple values in it 
#print(pytesseract.image_to_string(img2)) 