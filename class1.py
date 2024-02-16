#reading and displaying image! RGB image
import cv2

#read the image
img = cv2.imread("cat.jpg")

print(img.shape)
print(img.ndim)

#to displlay the image
# cv2.imshow("image",img)


# cv2.waitKey(3000)
while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()

