import cv2
import numpy as np


# Bước 2: Đọc ảnh RGB
img = cv2.imread('com ga nam.jpg', cv2.IMREAD_COLOR)

# Bước 3: Hiển thị ảnh RGB
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bước 4: Chuyển ảnh về đa cấp xám theo phương pháp Lightness
img_gray1 = (np.min(img, axis=2) + np.max(img, axis=2)) // 2

# Hiển thị ảnh img_gray1
cv2.imshow('Grayscale (Lightness)', img_gray1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bước 5: Chuyển ảnh về đa cấp xám theo phương pháp Average
img_gray2 = np.mean(img, axis=2, dtype=np.uint8)

# Hiển thị ảnh img_gray2
cv2.imshow('Grayscale (Average)', img_gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bước 6: Chuyển ảnh về đa cấp xám theo phương pháp Luminosity
img_gray3 = np.dot(img[..., :3], [0.3, 0.59, 0.11]).astype(np.uint8)

# Hiển thị ảnh img_gray3
cv2.imshow('Grayscale (Luminosity)', img_gray3)
cv2.waitKey(0)
cv2.destroyAllWindows()
