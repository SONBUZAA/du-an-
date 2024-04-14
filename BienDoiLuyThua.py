import cv2
import numpy as np
from gamma_corrected import gamma_corrected
from window_title import window_title

# Open the image.
img = cv2.imread('com ga nam.jpg')
cv2.imshow("Input image", img)

# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2]:
    # Apply gamma correction to the image.
    gamma_corrected_img = gamma_corrected(img, gamma)

    # Display the gamma corrected image.
    cv2.imshow(window_title, gamma_corrected_img)
    cv2.waitKey(0)

    # Save edited images.
    cv2.imwrite('gamma_transformed_' + str(gamma) + '.jpg', gamma_corrected_img)

cv2.destroyAllWindows()
