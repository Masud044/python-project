import cv2
import numpy as np

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
   

    noisy_image = np.copy(image)
    total_pixels = image.size // image.shape[2]
    
    
    num_salt = int(np.ceil(salt_prob * total_pixels))
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1], :] = 255

    # Add pepper noise (black pixels)
    num_pepper = int(np.ceil(pepper_prob * total_pixels))
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1], :] = 0

    return noisy_image


image_path = "images1.jpeg"  
image = cv2.imread(image_path, cv2.IMREAD_COLOR)


if image is None:
    print("Error: Could not load image. Please check the file path.")
else:
    
    salt_prob = 0.02  
    pepper_prob = 0.02  
    noisy_image = add_salt_and_pepper_noise(image, salt_prob, pepper_prob)

    
    filtered_image = cv2.medianBlur(noisy_image, 5)  

    
    cv2.imshow("Original Image", image)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()