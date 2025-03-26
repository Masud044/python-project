import cv2
import numpy as np


image_path = 'nature.jpeg'  
image = cv2.imread(image_path)


mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.rectangle(mask, (50, 50), (200, 200), 255, -1)  


inpaint_result = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)


cv2.imwrite('result.jpg', inpaint_result)
cv2.imshow('Original', image)
cv2.imshow('Mask', mask)
cv2.imshow('Result', inpaint_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
