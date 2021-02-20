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

#mean-shift
ms = MeanShift(bandwidth = 7)
   
ms.fit(Z)
 
labels=ms.labels_
    
cluster_centers = ms.cluster_centers_

   
labels_unique = np.unique(labels)    
n_clusters_ = len(labels_unique)    
print("number of estimated clusters : %d" % n_clusters_)    

result = []
for i in labels:
    result.append(cluster_centers[i])
result = np.reshape(result, originShape)
result = color.lab2rgb(result)

plt.imshow(result)
plt.show()


