import cv2

image_path = 'com ga nam.jpg'


image_bgr = cv2.imread(image_path)
cv2.imshow('com ga nam.jpg - BGR', image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()


image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
output_path_rgb = 'com_ga_nam_rgb.jpg'  
cv2.imwrite(output_path_rgb, cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)) 


cv2.imshow('com ga nam.jpg - RGB', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()


image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
cv2.imshow('com ga nam.jpg - HSV', image_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()


image_yuv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YUV)
cv2.imshow('com ga nam.jpg - YUV', image_yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()
