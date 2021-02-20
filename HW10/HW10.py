import cv2
import numpy as np
import matplotlib.pyplot as plt

x1 = [0, 0, 0, 0, 0]
y1 = [0, 0, 0, 0, 0]
max1 = [0., 0., 0., 0., 0.]
x = []

def check_if_true(a):
    ret = True
    if abs(x[1] - a[32+x1[0]][32+y1[0]]) > max1[0] + 10:
        ret = False
    if abs(x[2] - a[32+x1[1]][32+y1[1]]) > max1[1] + 10:
        ret = False
    if abs(x[3] - a[32+x1[2]][32+y1[2]]) > max1[2] + 10:
        ret = False
    if abs(x[4] - a[32+x1[3]][32+y1[3]]) > max1[3] + 10:
        ret = False
    if abs(x[5] - a[32+x1[4]][32+y1[4]]) > max1[4] + 10:
        ret = False
    return ret

p1 = cv2.imread("picture1.jpg", 0)
p1_1 = p1[:64, :64]
f1 = np.fft.fft2(p1_1)
fshift1 = np.fft.fftshift(f1)
magnitude1_1 = 20*np.log(np.abs(fshift1))

p1_2 = p1[40 : 104, :64]
f2 = np.fft.fft2(p1_2)
fshift2 = np.fft.fftshift(f2)
magnitude1_2 = 20*np.log(np.abs(fshift2))

p1_3 = p1[:64, 40 : 104]
f3 = np.fft.fft2(p1_3)
fshift3 = np.fft.fftshift(f3)
magnitude1_3 = 20*np.log(np.abs(fshift3))

p1_4 = p1[40 : 104, 40 : 104]
f4 = np.fft.fft2(p1_4)
fshift4 = np.fft.fftshift(f4)
magnitude1_4 = 20*np.log(np.abs(fshift4))

p1_5 = p1[:64, 20:84]
f5 = np.fft.fft2(p1_5)
fshift5 = np.fft.fftshift(f5)
magnitude1_5 = 20*np.log(np.abs(fshift5))

magnitude1 = magnitude1_1 + magnitude1_2 + magnitude1_3 + magnitude1_4 + magnitude1_5
magnitude1 /= 5
dx = magnitude1[32:64, 32:64]

for i in range(32):
    for j in range(32):
        x.append(dx[i][j])
x.sort(reverse=True)
for i in range(32):
    for j in range(32):
        if dx[i][j] == x[1]:
            x1[0] = i
            y1[0] = j
        elif dx[i][j] == x[2]:
            x1[1] = i
            y1[1] = j
        elif dx[i][j] == x[3]:
            x1[2] = i
            y1[2] = j
        elif dx[i][j] == x[4]:
            x1[3] = i
            y1[3] = j
        elif dx[i][j] == x[5]:
            x1[4] = i
            y1[4] = j
            
max1[0] = abs(x[1] - magnitude1_1[32+x1[0]][32+y1[0]])
max1[1] = abs(x[2] - magnitude1_1[32+x1[1]][32+y1[1]])
max1[2] = abs(x[3] - magnitude1_1[32+x1[2]][32+y1[2]])
max1[3] = abs(x[4] - magnitude1_1[32+x1[3]][32+y1[3]])
max1[4] = abs(x[5] - magnitude1_1[32+x1[4]][32+y1[4]])

max1[0] = max(max1[0], abs(x[1] - magnitude1_2[32+x1[0]][32+y1[0]]))
max1[1] = max(max1[1], abs(x[2] - magnitude1_2[32+x1[1]][32+y1[1]]))
max1[2] = max(max1[2], abs(x[3] - magnitude1_2[32+x1[2]][32+y1[2]]))
max1[3] = max(max1[3], abs(x[4] - magnitude1_2[32+x1[3]][32+y1[3]]))
max1[4] = max(max1[4], abs(x[5] - magnitude1_2[32+x1[4]][32+y1[4]]))

max1[0] = max(max1[0], abs(x[1] - magnitude1_3[32+x1[0]][32+y1[0]]))
max1[1] = max(max1[1], abs(x[2] - magnitude1_3[32+x1[1]][32+y1[1]]))
max1[2] = max(max1[2], abs(x[3] - magnitude1_3[32+x1[2]][32+y1[2]]))
max1[3] = max(max1[3], abs(x[4] - magnitude1_3[32+x1[3]][32+y1[3]]))
max1[4] = max(max1[4], abs(x[5] - magnitude1_3[32+x1[4]][32+y1[4]]))

max1[0] = max(max1[0], abs(x[1] - magnitude1_4[32+x1[0]][32+y1[0]]))
max1[1] = max(max1[1], abs(x[2] - magnitude1_4[32+x1[1]][32+y1[1]]))
max1[2] = max(max1[2], abs(x[3] - magnitude1_4[32+x1[2]][32+y1[2]]))
max1[3] = max(max1[3], abs(x[4] - magnitude1_4[32+x1[3]][32+y1[3]]))
max1[4] = max(max1[4], abs(x[5] - magnitude1_4[32+x1[4]][32+y1[4]]))

max1[0] = max(max1[0], abs(x[1] - magnitude1_5[32+x1[0]][32+y1[0]]))
max1[1] = max(max1[1], abs(x[2] - magnitude1_5[32+x1[1]][32+y1[1]]))
max1[2] = max(max1[2], abs(x[3] - magnitude1_5[32+x1[2]][32+y1[2]]))
max1[3] = max(max1[3], abs(x[4] - magnitude1_5[32+x1[3]][32+y1[3]]))
max1[4] = max(max1[4], abs(x[5] - magnitude1_5[32+x1[4]][32+y1[4]]))

for i in range(20):
    print("picture", i+1)
    pic = "picture" + str(i + 1) + ".jpg"
    p1 = cv2.imread(pic, 0)

    t1_1 = p1[30:94, 30:94]
    tf1 = np.fft.fft2(t1_1)
    tfshift1 = np.fft.fftshift(tf1)
    tmagnitude1_1 = 20*np.log(np.abs(tfshift1))
    print(check_if_true(tmagnitude1_1))

    t1_2 = p1[21:85, 40:104]
    tf2 = np.fft.fft2(t1_2)
    tfshift2 = np.fft.fftshift(tf2)
    tmagnitude1_2 = 20*np.log(np.abs(tfshift2))
    print(check_if_true(tmagnitude1_2))

    t1_3 = p1[50:114, 80:144]
    tf3 = np.fft.fft2(t1_3)
    tfshift3 = np.fft.fftshift(tf3)
    tmagnitude1_3 = 20*np.log(np.abs(tfshift3))
    print(check_if_true(tmagnitude1_3))

    t1_4 = p1[40:104, 30:94]
    tf4 = np.fft.fft2(t1_4)
    tfshift4 = np.fft.fftshift(tf4)
    tmagnitude1_4 = 20*np.log(np.abs(tfshift4))
    print(check_if_true(tmagnitude1_4))

    t1_5 = p1[60:124, 60:124]
    tf5 = np.fft.fft2(t1_5)
    tfshift5 = np.fft.fftshift(tf5)
    tmagnitude1_5 = 20*np.log(np.abs(tfshift5))
    print(check_if_true(tmagnitude1_5))

    print()

plt.imshow(magnitude1_1, cmap = 'gray')
plt.show()

plt.imshow(magnitude1_2, cmap = 'gray')
plt.show()

plt.imshow(magnitude1_3, cmap = 'gray')
plt.show()

plt.imshow(magnitude1_4, cmap = 'gray')
plt.show()

plt.imshow(magnitude1_5, cmap = 'gray')
plt.show()

plt.imshow(magnitude1, cmap = 'gray')
plt.show()

