import cv2

# Đọc ảnh xám từ file
y = cv2.imread('com ga nam.jpg' )
y_gray= cv2.cvtColor(y, cv2.COLOR_BGR2GRAY)
if y is not None:
    # Hiển thị ảnh xám gốc
    cv2.imshow('Ảnh GrayScale', y_gray)

    # Tạo ảnh âm bản sử dụng hàm cv2.bitwise_not()
    y_amban = cv2.bitwise_not(y_gray)

    # Hiển thị ảnh âm bản
    cv2.imshow('Ảnh Âm Bản', y_amban)
    cv2.waitKey(0)

    # Đóng cửa sổ khi nhấn một phím bất kỳ
    cv2.destroyAllWindows()
else:
    print("Không thể đọc được ảnh. Hãy chắc chắn rằng tên file và đường dẫn là chính xác.")
