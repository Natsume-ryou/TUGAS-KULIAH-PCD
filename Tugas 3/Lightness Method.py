import cv2
import numpy as np


img = cv2.imread('Gambar/Kaori.jpg',0)

def toGrayWithLightness(img):
    gray = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gray[i][j] = (max(img[i][j][0], img[i][j][1], img[i][j][2]) + min(img[i][j][0], img[i][j][1], img[i][j][2])) / 2
    return gray


cv2.imwrite('Gambar/Hasil lightness.jpg', img)
cv2.waitKey(0)