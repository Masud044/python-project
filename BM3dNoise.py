import numpy as np
import matplotlib.pyplot as plt
from skimage import io, img_as_float
import bm3d


noisy_img = img_as_float(io.imread('noisy.jpg'))  


denoised_img_bm3d = np.zeros_like(noisy_img)
for i in range(3):  
    denoised_img_bm3d[:, :, i] = bm3d.bm3d(noisy_img[:, :, i], sigma_psd=0.2, stage_arg=bm3d.BM3DStages.HARD_THRESHOLDING)


plt.figure(figsize=(15, 10))

# Noisy Image
plt.subplot(1, 3, 1)
plt.imshow(noisy_img)
plt.title("Image")
plt.axis("off")

# BM3D Denoised Image
plt.subplot(1, 3, 2)
plt.imshow(denoised_img_bm3d)
plt.title("Image Restoration")
plt.axis("off")

plt.show()
