import cv2
from matplotlib import pyplot as plt

img = cv2.imread("storage/cat.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
plt.subplot(1, 1, 1)
plt.imshow(img_gray)
plt.axis('off')
plt.show()
