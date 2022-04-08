import cv2
import numpy as np

img = cv2.imread('Gambar/Kaori.jpg')

def toGrayWithLuminosity(img):
    gray = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gray[i][j] = 0.21 * img[i][j][0] + 0.72 * img[i][j][1] + 0.07 * img[i][j][2]
    return gray
    
cv2.imwrite('Gambar/Hasil luminosity.jpg', img)
cv2.waitKey(0)