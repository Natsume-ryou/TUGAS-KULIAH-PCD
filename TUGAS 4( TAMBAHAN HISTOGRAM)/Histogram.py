import cv2
import numpy as np
import matplotlib.pyplot as plt

#Read image from library 
img = cv2.imread('Gambar/Maki san.jpg')

#Calculate frequency of each pixel value

histogram = cv2.calcHist([img],[0],None,[256],[0,256])

#show plotting graph of an image

plt.plot(histogram)
plt.show()