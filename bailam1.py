import cv2

# Đọc ảnh từ tệp JPG
image_path = 'com ga nam.jpg'
image_bgr = cv2.imread(image_path)

# Hiển thị ảnh (nếu bạn muốn)
cv2.imshow('com ga nam.jpg', image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
