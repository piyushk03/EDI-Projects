import easyocr
import cv2
from matplotlib import pyplot as plt
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# #print(voices[1].id)
# engine.setProperty('voice', voices[0].id) # you can change to female voice just by replacing 0 by 1 in voices[0].
# def speak(audio):
#         engine.say(audio)
#         engine.runAndWait()


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
#         img_name = "opencv_frame.png"
#         print(img_name)
#         img_path = os.path.join("D:\\Piyush\\SEM 1\\PycharmProjects\\pythonProject\\images",img_name)
#         cv2.imwrite(img_name,frame)
#         img_counter+=1

# cam.release()
# # cam.destroyAllWindows()



reader = easyocr.Reader(['en'],gpu=True)
result = reader.readtext("D:\Piyush\SEM 1\PycharmProjects\pythonProject\images\images.jpeg")

#print(result)

top_left = tuple(result[0][0][0])
print(top_left)
bottom_right = tuple(result[0][0][2])
print(bottom_right)
text = result[0][1]
# speak(text)
font = cv2.FONT_HERSHEY_SIMPLEX


img = cv2.imread("D:\Piyush\SEM 1\PycharmProjects\pythonProject\images\images.jpeg")
img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),4)
img = cv2.putText(img,text,top_left,font,.5,(255,0,0),2,cv2.LINE_AA)
plt.imshow(img)
plt.show()
