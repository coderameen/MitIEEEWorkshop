#To convert RGB to Binary Scale Image
import cv2
# img = cv2.imread("cat.jpg",0)#method 1
img = cv2.imread("cat.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#method 2
# print(gray_img.ndim)#2 channel

ret,binary = cv2.threshold(gray_img,150,255,cv2.THRESH_BINARY)
cv2.imshow("this is cat BINARY image",binary)

cv2.waitKey(0)
cv2.destroyAllWindows()