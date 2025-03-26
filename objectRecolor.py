import cv2
import numpy as np


image = cv2.imread('nature1.jpeg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)


contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


new_color = [0, 0, 255]  

for contour in contours:
    
    mask = np.zeros_like(image)  

    cv2.drawContours(mask, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    
    mask = mask[:, :, 0]  

    
    image[mask == 255] = new_color


cv2.imshow('Original Image', cv2.imread('nature1.jpeg'))
cv2.imshow('Recolored Image', image)


cv2.imwrite('recolored_image.jpg', image)


cv2.waitKey(0)
cv2.destroyAllWindows()
