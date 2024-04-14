# Viet chuong trinh nhap vao 1 anh y bat ky hien thi anh y ra man hinh 
# chuyển đổi anh y sang y phẩy . hiển thị y phẩy

# Viet chương trinh nap vao 1 anh y bất kì . hiển thi y
# y về ảnh graycsrace . hiển thị y
# tìm ảnh âm bản y . hiển thị y phẩy ra màn hinh

import cv2

# Đọc ảnh từ tệp JPG

y= cv2.imread('com ga nam.jpg')
cv2.imshow('com ga nam.jpg', y)
gray_image = cv2.cvtColor(y, cv2.COLOR_BGR2GRAY)
cv2.imshow('Am Ban', gray_image)
gray_image1 = cv2.cvtColor(gray_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Am Ban 1', gray_image1)
cv2.waitKey(0)

cv2.destroyAllWindows()