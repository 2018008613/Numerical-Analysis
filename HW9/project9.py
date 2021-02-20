import os
import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
import math

def C(x):
    if x == 0:
        return 1/math.sqrt(2)
    return 1

n = cv2.imread("picture1.jpg")
n = np.array(n)
an = np.zeros((256,256,3))
SR = np.zeros((256,256))
SG = np.zeros((256,256))
SB = np.zeros((256,256))

for i in range(256):
    for j in range(256):
        SR[i][j] = n[i][j][2]
        SG[i][j] = n[i][j][1]
        SB[i][j] = n[i][j][0]

sr = np.zeros((16,16))
sg = np.zeros((16,16))
sb = np.zeros((16,16))
fr = np.zeros((16,16))
fg = np.zeros((16,16))
fb = np.zeros((16,16))

afr = np.zeros(256)
afg = np.zeros(256)
afb = np.zeros(256)

for i in range(16):
    for j in range(16):
        for u in range(16):
            for v in range(16):
                sr[u][v] = SR[u + i * 16][v + j * 16]
                sg[u][v] = SG[u + i * 16][v + j * 16]
                sb[u][v] = SB[u + i * 16][v + j * 16]

        for u in range(16):
            for v in range(16):
                fr[u][v] = C(u)*C(v) / 4
                fg[u][v] = C(u)*C(v) / 4
                fb[u][v] = C(u)*C(v) / 4
                gr = 0
                gg = 0
                gb = 0
                for x in range(16):
                    for y in range(16):
                        gr += sr[x][y] * np.cos(u * math.pi * (2 * x + 1) / 32) * np.cos(v * math.pi * (2 * y + 1) / 32)
                        gg += sg[x][y] * np.cos(u * math.pi * (2 * x + 1) / 32) * np.cos(v * math.pi * (2 * y + 1) / 32)
                        gb += sb[x][y] * np.cos(u * math.pi * (2 * x + 1) / 32) * np.cos(v * math.pi * (2 * y + 1) / 32)
                fr[u][v] *= gr
                fg[u][v] *= gg
                fb[u][v] *= gb

        for x in range(16):
            for y in range(16):
                afr[x * 16 + y] = abs(fr[x][y])
                afg[x * 16 + y] = abs(fg[x][y])
                afb[x * 16 + y] = abs(fb[x][y])
        afr = np.sort(afr)[::-1]
        afg = np.sort(afg)[::-1]
        afb = np.sort(afb)[::-1]

        for x in range(16):
            for y in range(16):
                if abs(fr[x][y]) < afr[15]:
                    fr[x][y] = 0
                if abs(fg[x][y]) < afg[15]:
                    fg[x][y] = 0
                if abs(fb[x][y]) < afb[15]:
                    fb[x][y] = 0

        for x in range(16):
            for y in range(16):
                sr[x][y] = 0
                sg[x][y] = 0
                sb[x][y] = 0

                for u in range(16):
                    for v in range(16):
                        sr[x][y] += C(u) * C(v) * fr[u][v] * np.cos(u * math.pi * (2 * x + 1) / 32) * np.cos(v * math.pi * (2 * y + 1) / 32)
                        sg[x][y] += C(u) * C(v) * fg[u][v] * np.cos(u * math.pi * (2 * x + 1) / 32) * np.cos(v * math.pi * (2 * y + 1) / 32)
                        sb[x][y] += C(u) * C(v) * fb[u][v] * np.cos(u * math.pi * (2 * x + 1) / 32) * np.cos(v * math.pi * (2 * y + 1) / 32)

                sr[x][y] /= 4
                sg[x][y] /= 4
                sb[x][y] /= 4

        max_r = np.max(sr)
        min_r = np.min(sr)
        max_g = np.max(sg)
        min_g = np.min(sg)
        max_b = np.max(sb)
        min_b = np.min(sb)

        for x in range(16):
            for y in range(16):
                if min_r < 0:
                    sr[x][y] -= min_r
                if max_r - min_r > 255:
                    sr[x][y] = sr[x][y] * 250 / (max_r - min_r)
                if min_g < 0:
                    sg[x][y] -= min_g
                if max_g - min_g > 255:
                    sg[x][y] = sg[x][y] * 250 / (max_g - min_g)
                if min_b < 0:
                    sb[x][y] -= min_b
                if max_b - min_b > 255:
                    sb[x][y] = sb[x][y] * 250 / (max_b - min_b)
                sr[x][y] = round(sr[x][y])
                sg[x][y] = round(sg[x][y])
                sb[x][y] = round(sb[x][y])
       
                SR[x + i * 16][y + j * 16] = sr[x][y]
                SG[x + i * 16][y + j * 16] = sg[x][y]
                SB[x + i * 16][y + j * 16] = sb[x][y]
                
for i in range(256):
    for j in range(256):
        an[i][j][2] = SR[i][j]
        an[i][j][1] = SG[i][j]
        an[i][j][0] = SB[i][j]

cv2.imwrite('p10.png', an)

        
