#To convert RGB to Gray Scale Image
import cv2
# img = cv2.imread("cat.jpg",0)#method 1
img = cv2.imread("cat.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#method 2
print(gray_img.ndim)#2 channel
cv2.imshow("this is cat gray image",gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#hello I am pushong the some changes