import numpy as np
import math

#5개의 중점과 각각의 분산값
#0(1) 0(1) 0(1)
#4(1) 0(2) 0(1)
#4(1) 8(2) 0(2)
#0(1) 8(2) 0(1)
#2(1.5) 4(1.5) 3(1)

#초기 중점 설정
 
centerx = [0, 4, 4, 0, 2]
centery = [0, 0, 8, 8 ,4]
centerz = [0, 0, 0, 0, 3]
max_len = [0, 0, 0, 0, 0]

#데이터로부터 idx번째 center까지의 거리를 구해주는 함수

def get_dis(vec, idx):
    return math.sqrt((vec[0]-centerx[idx])*(vec[0]-centerx[idx]) + (vec[1]-centery[idx])*(vec[1]-centery[idx]) + (vec[2]-centerz[idx])*(vec[2]-centerz[idx]))


#중점마다 300개씩 총 1500개의 데이터를 생성해 n에 저장함
n = []
sigma, mu = 1, 0
x = sigma * np.random.randn(300) + mu
y = sigma * np.random.randn(300) + mu
z = sigma * np.random.randn(300) + mu

for i in range(300):
    n.append([x[i],y[i],z[i]])

sigma, mu = 1, 4
x = sigma * np.random.randn(300) + mu
sigma, mu = 2, 0
y = sigma * np.random.randn(300) + mu
sigma, mu = 1, 0
z = sigma * np.random.randn(300) + mu

for i in range(300):
    n.append([x[i],y[i],z[i]])

sigma, mu = 1, 4
x = sigma * np.random.randn(300) + mu
sigma, mu = 2, 8
y = sigma * np.random.randn(300) + mu
sigma, mu = 2, 0
z = sigma * np.random.randn(300) + mu

for i in range(300):
    n.append([x[i],y[i],z[i]])

sigma, mu = 1, 0
x = sigma * np.random.randn(300) + mu
sigma, mu = 2, 8
y = sigma * np.random.randn(300) + mu
sigma, mu = 1, 0
z = sigma * np.random.randn(300) + mu

for i in range(300):
    n.append([x[i],y[i],z[i]])

sigma, mu = 1.5, 2
x = sigma * np.random.randn(300) + mu
sigma, mu = 1.5, 4
y = sigma * np.random.randn(300) + mu
sigma, mu = 1.5, 3
z = sigma * np.random.randn(300) + mu

for i in range(300):
    n.append([x[i],y[i],z[i]])

#10번의 K-means clustering을 통해 중점을 조정해주고
#cluster에서 cluster 내부 데이터와의 최대 거리를 계산해줌

for i in range(10):
    max_len = [0, 0, 0, 0, 0]
    cluster0 = []
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []

    for v in n:
        this_cluster = -1
        this_len = 99999999
        for i in range(5):
            d = get_dis(v,i)
            if this_len > d:
                this_cluster = i
                this_len = d
        max_len[this_cluster] = max(max_len[this_cluster], this_len)
        if this_cluster == 0:
            cluster0.append(v)
        elif this_cluster == 1:
            cluster1.append(v)
        elif this_cluster == 2:
            cluster2.append(v)
        elif this_cluster == 3:
            cluster3.append(v)
        else:
            cluster4.append(v)

    v = [0,0,0]
    if len(cluster0) > 0:
        for t in cluster0:
            v[0] += t[0]
            v[1] += t[1]
            v[2] += t[2]
        v[0] /= len(cluster0)
        v[1] /= len(cluster0)
        v[2] /= len(cluster0)
        centerx[0] = v[0]
        centery[0] = v[1]
        centerz[0] = v[2]
    v = [0,0,0]
    if len(cluster1) > 0:
        for t in cluster1:
            v[0] += t[0]
            v[1] += t[1]
            v[2] += t[2]
        v[0] /= len(cluster1)
        v[1] /= len(cluster1)
        v[2] /= len(cluster1)
        centerx[1] = v[0]
        centery[1] = v[1]
        centerz[1] = v[2]
    v = [0,0,0]
    if len(cluster2) > 0:
        for t in cluster2:
            v[0] += t[0]
            v[1] += t[1]
            v[2] += t[2]
        v[0] /= len(cluster2)
        v[1] /= len(cluster2)
        v[2] /= len(cluster2)
        centerx[2] = v[0]
        centery[2] = v[1]
        centerz[2] = v[2]
    v = [0,0,0]
    if len(cluster3) > 0:
        for t in cluster3:
            v[0] += t[0]
            v[1] += t[1]
            v[2] += t[2]
        v[0] /= len(cluster3)
        v[1] /= len(cluster3)
        v[2] /= len(cluster3)
        centerx[3] = v[0]
        centery[3] = v[1]
        centerz[3] = v[2]
    v = [0,0,0]
    if len(cluster4) > 0:
        for t in cluster4:
            v[0] += t[0]
            v[1] += t[1]
            v[2] += t[2]
        v[0] /= len(cluster4)
        v[1] /= len(cluster4)
        v[2] /= len(cluster4)
        centerx[4] = v[0]
        centery[4] = v[1]
        centerz[4] = v[2]

#각각의 cluster마다 test해서 num에서는 idx번째 cluster로 분류된 데이터의 개수를
#각각 저장해서 출력함. 마지막 idx는 거리가 기준을 초과해서 해당 cluster로
#분류되지 못한 데이터의 수

n = []
sigma, mu = 1, 0
x = sigma * np.random.randn(100) + mu
y = sigma * np.random.randn(100) + mu
z = sigma * np.random.randn(100) + mu

for i in range(100):
    n.append([x[i],y[i],z[i]])

num = [0, 0, 0, 0, 0, 0]
print("cluster0")
for v in n:
    this_cluster = -1
    this_len = 99999999
    for i in range(5):
        d = get_dis(v,i)
        if this_len > d:
            this_cluster = i
            this_len = d
    if this_len > max_len[this_cluster]:
        num[5] += 1
    else:
        num[this_cluster] += 1
print(num)

n = []
sigma, mu = 1, 4
x = sigma * np.random.randn(100) + mu
sigma, mu = 2, 0
y = sigma * np.random.randn(100) + mu
sigma, mu = 1, 0
z = sigma * np.random.randn(100) + mu

for i in range(100):
    n.append([x[i],y[i],z[i]])

num = [0, 0, 0, 0, 0, 0]
print("cluster1")
for v in n:
    this_cluster = -1
    this_len = 99999999
    for i in range(5):
        d = get_dis(v,i)
        if this_len > d:
            this_cluster = i
            this_len = d
    if this_len > max_len[this_cluster]:
        num[5] += 1
    else:
        num[this_cluster] += 1
print(num)

n = []
sigma, mu = 1, 4
x = sigma * np.random.randn(100) + mu
sigma, mu = 2, 8
y = sigma * np.random.randn(100) + mu
sigma, mu = 2, 0
z = sigma * np.random.randn(100) + mu

for i in range(100):
    n.append([x[i],y[i],z[i]])

num = [0, 0, 0, 0, 0, 0]
print("cluster2")
for v in n:
    this_cluster = -1
    this_len = 99999999
    for i in range(5):
        d = get_dis(v,i)
        if this_len > d:
            this_cluster = i
            this_len = d
    if this_len > max_len[this_cluster]:
        num[5] += 1
    else:
        num[this_cluster] += 1
print(num)

n = []
sigma, mu = 1, 0
x = sigma * np.random.randn(100) + mu
sigma, mu = 2, 8
y = sigma * np.random.randn(100) + mu
sigma, mu = 1, 0
z = sigma * np.random.randn(100) + mu

for i in range(100):
    n.append([x[i],y[i],z[i]])

num = [0, 0, 0, 0, 0, 0]
print("cluster3")
for v in n:
    this_cluster = -1
    this_len = 99999999
    for i in range(5):
        d = get_dis(v,i)
        if this_len > d:
            this_cluster = i
            this_len = d
    if this_len > max_len[this_cluster]:
        num[5] += 1
    else:
        num[this_cluster] += 1
print(num)

n = []
sigma, mu = 1.5, 2
x = sigma * np.random.randn(100) + mu
sigma, mu = 1.5, 4
y = sigma * np.random.randn(100) + mu
sigma, mu = 1.5, 3
z = sigma * np.random.randn(100) + mu

for i in range(100):
    n.append([x[i],y[i],z[i]])

num = [0, 0, 0, 0, 0, 0]
print("cluster4")
for v in n:
    this_cluster = -1
    this_len = 99999999
    for i in range(5):
        d = get_dis(v,i)
        if this_len > d:
            this_cluster = i
            this_len = d
    if this_len > max_len[this_cluster]:
        num[5] += 1
    else:
        num[this_cluster] += 1
print(num)

n = []
sigma, mu = 1, 2
x = sigma * np.random.randn(100) + mu
sigma, mu = 1, 4
y = sigma * np.random.randn(100) + mu
sigma, mu = 1, -5
z = sigma * np.random.randn(100) + mu

for i in range(100):
    n.append([x[i],y[i],z[i]])

num = [0, 0, 0, 0, 0, 0]
print("another")
for v in n:
    this_cluster = -1
    this_len = 99999999
    for i in range(5):
        d = get_dis(v,i)
        if this_len > d:
            this_cluster = i
            this_len = d
    if this_len > max_len[this_cluster]:
        num[5] += 1
    else:
        num[this_cluster] += 1
print(num)

    
