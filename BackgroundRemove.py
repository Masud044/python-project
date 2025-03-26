import cv2
import numpy as np


image = cv2.imread('nature1.jpeg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


mask = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)


inverted_mask = cv2.bitwise_not(mask)


background_removed = cv2.bitwise_and(image, image, mask=mask)


background_color = (255, 255, 255)  # White
background = np.full_like(image, background_color)
result = np.where(background_removed == 0, background, background_removed)




mask = np.zeros(image.shape[:2], np.uint8)


bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)


rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)


cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)


mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
result = image * mask[:, :, np.newaxis]


cv2.imwrite('grabcut_result.jpg', result)
cv2.imshow('GrabCut Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

