import cv2
import numpy as np
from matplotlib import pylab as plt


image = cv2.imread('images.jpeg')


dst = cv2.fastNlMeansDenoisingColored(image, None, 20,15,7,21)



row,col = 1,2
fig, axs = plt.subplots(row,col,figsize=(15,5))

fig.tight_layout()

axs[0].imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
axs[0].set_title('Noise Image')
axs[1].imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
axs[1].set_title('Denoise Image')
plt.show()

