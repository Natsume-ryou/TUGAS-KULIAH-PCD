import cv2
import numpy as np

#create image
img = np.zeros((5,4),dtype=np.uint8)
for i in range (img.shape[1]):
    for j in range (img.shape[0]):
        img[j,i] = i


#change every pixel

img [0,0] = 29
img [0,1] = 10
img [0,2] = 12
img [0,3] = 13
img [1,0] = 34
img [1,1] = 12
img [1,2] = 13
img [1,3] = 13
img [2,0] = 31
img [2,1] = 10
img [2,2] = 11
img [2,3] = 12
img [3,0] = 30
img [3,1] = 11
img [3,2] = 14
img [3,3] = 14
img [4,0] = 31
img [4,1] = 12
img [4,2] = 12
img [4,3] = 11

#use lowpass filter

x = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
lowpass = cv2.filter2D(src = img, ddepth =-1, kernel = x)

print("Before:",img)
print("After:",lowpass)