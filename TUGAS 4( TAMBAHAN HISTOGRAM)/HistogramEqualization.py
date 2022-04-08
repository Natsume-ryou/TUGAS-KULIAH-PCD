#import library 
import cv2
import numpy as np

#Read image from library
img =  cv2.imread('Gambar/Kaori.jpg',0)

#creating a histogram equalization when use method cv2.equalizeHist()
equ_img = cv2.equalizeHist(img)

#stack image
res_img = np.hstack((img,equ_img))

#show image
cv2.imshow("hasil gambar", res_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
