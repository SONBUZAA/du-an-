import cv2
import numpy as np
img=cv2.imread('com ga nam.jpg')
cv2.imshow("Origanal",img)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("RGB",img2)
R, G, B = cv2.split(img)
img_gray1 = ((np.maximum(np.maximum(R, G), B) + np.minimum(np.minimum(R, G), B)) / 2).astype(np.uint8)
cv2.imshow("lightness",img_gray1)
print(R)
img_gray2 = ((R+G+B)/3).astype(np.uint8)
cv2.imshow("average",img_gray2)
img_gray3 = ((R*0.3+G*0.59+B*0.11)/3).astype(np.uint8)
cv2.imshow("luminosity",img_gray3)

img_4=cv2.merge((R,G,B))
cv2.imshow("MEGER",img_4)
cv2.waitKey(0)
cv2.destroyAllWindows()