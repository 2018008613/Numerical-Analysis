import numpy as np
from sklearn.model_selection import train_test_split

def gaussian_noise(x):
    return (1 / np.sqrt(2 * np.pi * 2)) * np.exp(- x ** 2 / 4)

dx = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
dy = [-11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11]
for i in range(12):
    dy[i] += gaussian_noise(dx[i])

A = np.zeros((6,2))
b = np.zeros(6)

for i in range(6):
    A[i][1] = 1

a = 0
c = 0
cost = 999999999

for t in range(10):
    x = list(range(12))
    x_train, x_test = train_test_split(x, test_size=0.5)

    for i in range(6):
        A[i][0] = dx[x_train[i]]
        b[i] = dy[x_train[i]]

    x = np.linalg.inv(A.T@A)@A.T@b

    this_cost = 0
    b1 = A @ x
    for i in range(6):
        this_cost += (b1[i]-dy[x_train[i]]) * (b1[i]-dy[x_train[i]])
    if cost > this_cost:
        a = x[0]
        c = x[1]
        cost = this_cost

A = np.zeros((12,2))
b = np.zeros(12)

for i in range(12):
    A[i][1] = 1
    A[i][0] = dx[i]

b = dy

x = np.linalg.inv(A.T@A)@A.T@b
a1 = x[0]
c1 = x[1]
print(a, c, a1, c1)
