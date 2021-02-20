import os
import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image

path = glob.glob("lfwcrop_grey/lfwcrop_grey/faces/*.pgm")
cv_img=[]
for img in path:
    n=cv2.imread(img, 0)
    n=n.ravel()
    cv_img.append(n)

m = []
for j in range(len(cv_img[0])):
    colsum = 0
    for i in range(len(cv_img)):
        colsum += cv_img[i][j]
    colsum /= len(cv_img)
    m.append(colsum)
for i in range(len(cv_img)):
    for j in range(len(cv_img[0])):
        cv_img[i][j] -= m[j]

test = np.array(cv_img).T
U, s, VT = np.linalg.svd(test)

c = U.T
eigen_num = 30

meanvector = np.array(m)
meanvector = meanvector.reshape(64, 64)
#plt.imshow(meanvector, cmap='gray')
#plt.show()
#for i in range(eigen_num):
#    eigenface = np.array(c[i])
#    eigenface = eigenface.reshape(64, 64)
#    plt.imshow(eigenface, cmap='gray')
#    plt.show()

path = glob.glob("test/*.pgm")
num = 0
for img in path:
    n=cv2.imread(img, 0)
    n=n.ravel()
    for i in range(4096):
        n[i] -= m[i]
    c_arr = []
    for i in range(eigen_num):
        x = c[i] @ n
        c_arr.append(x)
    print(num + 1)
    print(c_arr)
    num = (num + 1) % 5
    facevector=c[0] * c_arr[0]
    for j in range(1,30):
        facevector += c[j] * c_arr[j]
    facevector += m
    facevector = np.array(facevector)
    facevector = facevector.reshape(64, 64)
    plt.imshow(facevector, cmap='gray')
    plt.show()
    
