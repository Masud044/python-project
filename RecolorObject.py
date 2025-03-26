import cv2
import numpy as np


image = cv2.imread('flower.jpeg')


hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower_color = np.array([0, 120, 70])  
upper_color = np.array([10, 255, 255])  


mask = cv2.inRange(hsv_image, lower_color, upper_color)


colored_image = image.copy()


new_color = [255, 0, 0] 


colored_image[mask == 255] = new_color


cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Colored Image', colored_image)


cv2.imwrite('colored_image.jpg', colored_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
