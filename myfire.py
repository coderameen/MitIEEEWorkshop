import cv2
#import cascade
from playsound import playsound
import pyttsx3

#text to speech
def my_speak():
    engine = pyttsx3.init()
    engine.say("Alert Fire has been detected!!! please run")
    engine.runAndWait()

fire_cascade = cv2.CascadeClassifier("fire_detection.xml")
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame,1.2,5)
    
    for x,y,w,h in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(0,255,0),3)
        roi_gray = gray[y:y+h,x:x+w]#region of interest
        roi_color = frame[y:y+h,x:x+w] #roi
        
        print("Fire is detected!!!")
        # playsound("audio.mp3")
        for i in range(3):
            my_speak()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == 13:
        break
# cap.release()
# cv2.destroyAllWindows() 


