#capture image from camera(internal) and display
import cv2
import matplotlib.pyplot as plt

#to access the camera
cap = cv2.VideoCapture(0)#0=>internal camera | 1=>external camera

ret,frame = cap.read()#to read/capture image
plt.imshow(frame)
plt.title("This is first image capture from camera")
plt.show()

#to off camera
cap.release()
