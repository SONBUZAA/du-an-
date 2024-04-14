import cv2
import numpy as np


img = cv2.imread('com ga nam.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


cv2.imshow('Original Image', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()


img_gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)[:, :, 2]
cv2.imshow('Gray Image (Lightness)', img_gray1)


img_gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image (Average)', img_gray2)


img_gray3 = np.dot(img_rgb[..., :3], [0.3, 0.59, 0.11]).astype(np.uint8)
cv2.imshow('Gray Image (Luminosity)', img_gray3)


cv2.waitKey(0)
cv2.destroyAllWindows()
