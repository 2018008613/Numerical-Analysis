from skimage import io, color
import matplotlib.pyplot as plt
import numpy as np
import cv2
from sklearn.cluster import MeanShift
from sklearn.datasets import make_blobs

rgb = io.imread("picture3.jpg")
lab = color.rgb2lab(rgb)

originShape = lab.shape
Z = lab.reshape((-1,3))

#k-means
Z = np.float32(Z)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 25
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

res = center[label.flatten()]
res2 = res.reshape((lab.shape))

result = color.lab2rgb(res2)

plt.imshow(result)
plt.show()
