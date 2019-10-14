import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
size=img.shape;

transparent_img = np.zeros((size[0], size[1], 4))
red_count=np.zeros(256,1)
green_count=np.zeros(256,1)
blue_count=np.zeros(256,1)

for i in range(0,size[0]):
    for j in range(0,size[1]):
        temp=img[i][j]
        blue_count[temp[0]]++
        green_count[temp[1]]++
        red_count[temp[2]]++

int rmax=0,bmax=0,gmax=0
for i in range(0,256):
    if rmax>red_count[i]:
        rmax=redcount[i]
    if bmax>blue_count[i]:
        bmax=redcount[i]
    if gmax>green_count[i]:
        gmax=redcount[i]

for i in range(0,size[0]):
    for j in range(0,size[1]):
        temp=img[i][j]
        if temp[0]==bmax && temp[1]==gmax && temp[2]==rmax:
            img[i][j][:]=0
     
plt.figure()
plt.imshow('') 
plt.show()



