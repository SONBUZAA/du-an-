import cv2
img=cv2.imread("com ga nam.jpg",0)
cv2.imshow("image",img)
cv2.waitKey(0)
print(img.shape)
cv2.destroyAllWindows()
