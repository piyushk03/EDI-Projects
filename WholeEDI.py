import cv2
import pytesseract
import pyttsx3 
import os

engine = pyttsx3.init('sapi5')#pyttsx3.init([driverName : string, debug : bool]) → pyttsx3.Engine Gets a reference to an engine instance that will use the given driver. sapi5 for Windows
voices = engine.getProperty('voices')#getProperty(name : string) → objectGets the current value of an engine property.To change the voice of the pyttsx3 engine, first, we will have to get the list of objects of voices.
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)#setProperty(name, value) → None # you can change to female voice just by replacing 0 by 1 in voices[0].The setProperty() function is used to set property based on a string.

img_name = ' '
def speak(audio):
        engine.say(audio)
        engine.setProperty('rate',250)
        engine.runAndWait()

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe" #To connect pytesseract to tesseract-which is pretrained library for OCR 
cam  = cv2.VideoCapture(0)

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
        img_name="opencv_frame.png"
        cv2.imwrite(img_name,frame)
        imgpath = os.path.join("D:\\Piyush\\SEM 1\\PycharmProjects\\pythonProject\\images",img_name)
        cv2.imwrite(imgpath,frame)
        print("screenshot taken")
        

img2 = cv2.imread("D:\\Piyush\\SEM 1\\PycharmProjects\\pythonProject\\images"+"\\"+str(img_name))
cv2.imshow("Image",img2)
cv2.waitKey(0)

h2Img , w2Img, _ = img2.shape #Gives height of an image relative to window, another value which we store in _ variable
#box2 = pytesseract.image_to_boxes(img2)
data2 = pytesseract.image_to_data(img2)

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
                print(a[11],end=' ')
                speak(a[11])
                #we need whole word which is stored at 11 index in array 

if cv2.waitKey(0) & 0xFF == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            cv2.waitKey(0)