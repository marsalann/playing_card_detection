import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread('C:\\Users\\arsal\\OneDrive\\Desktop\\WhatsApp Image 2023-04-09 at 01.53.16.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Canny edge detection to the blurred image
edges = cv2.Canny(blur, 100, 200)

# Display the original and resulting images
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])
plt.show()
