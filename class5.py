#to detect face from img
import cv2

#to import dataset-cascade(haarcascade dataset)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("group_img.jpg")#rgb image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#find cooridnates of the gray img
face = cascade.detectMultiScale(gray,1.04,6)

for x,y,w,h in face:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    
cv2.imshow("face detect in image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
