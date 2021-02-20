import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import copy

for i in range(1):
    #print("picture", i+1)
    #pic = "picture" + str(i + 1) + ".jpg"
    n = cv2.imread("picture8.jpg")
    yuv = cv2.cvtColor(n, cv2.COLOR_BGR2YUV)
    yuv1 = copy.deepcopy(yuv)
    yuv2 = copy.deepcopy(yuv)

    xs = len(n)
    ys = len(n[0])  
    
    n = np.array(n)
    nr = np.zeros((xs,ys,3))
    ng = np.zeros((xs,ys,3))
    nb = np.zeros((xs,ys,3))
    SR = np.zeros((xs,ys))
    SG = np.zeros((xs,ys))
    SB = np.zeros((xs,ys))
    Y = []
    U = []
    V = []

    for i in range(xs):
        for j in range(ys):
            SR[i][j] = n[i][j][2]
            SG[i][j] = n[i][j][1]
            SB[i][j] = n[i][j][0]
            nr[i][j][2] = n[i][j][2]
            ng[i][j][1] = n[i][j][1]
            nb[i][j][0] = n[i][j][0]
            yuv1[i][j][0] = yuv1[i][j][1]
            yuv1[i][j][1] = 0
            yuv1[i][j][2] = 0
            yuv2[i][j][0] = 0
            yuv2[i][j][1] = 0
            Y.append(yuv[i][j][0])
            U.append(yuv[i][j][1])
            V.append(yuv[i][j][2])

    cv2.imshow('Y', yuv[:,:,0])
    cv2.imshow('U', yuv1)
    cv2.imshow('V', yuv2)
    
    nr = nr.astype(np.int64)
    ng = ng.astype(np.int64)
    nb = nb.astype(np.int64)
    nr = list(np.array(nr))
    ng = list(ng)
    nb = list(nb)
    
    plt.imshow(nr)
    plt.show()
    plt.imshow(ng)
    plt.show()
    plt.imshow(nb)
    plt.show()

    SR = SR.astype(np.int64)
    SG = SG.astype(np.int64)
    SB = SB.astype(np.int64)
    SR = list(SR)
    SG = list(SG)
    SB = list(SB)
    R = []
    for i in range(xs):
        for j in range(ys):
            R.append(SR[i][j])
    G = []
    for i in range(xs):
        for j in range(ys):
            G.append(SG[i][j])
    B = []
    for i in range(xs):
        for j in range(ys):
            B.append(SB[i][j])
    arr = [R, G, B]

    df = pd.DataFrame(arr).T
    corr = df.corr(method = 'pearson')
    print(corr)

    yuvarr = [Y, U, V]
    yuvdf = pd.DataFrame(yuvarr).T
    yuvcorr = yuvdf.corr(method = 'pearson')
    print(yuvcorr)

    
