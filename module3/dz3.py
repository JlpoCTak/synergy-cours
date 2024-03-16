import matplotlib.pyplot as plt
import numpy as np


x1 = np.random.randint(100, size=100)
x2 = np.random.randint(200, size=100)
y = 3 * x1 + 2 * x2 - 1
x1 = x1 + np.random.randint(5, size=100) / 10
x2 = x2 + np.random.randint(5, size=100) / 10
y = y + np.random.randint(5, size=100) / 10

lr = 0.00004
w0 = 0
w1 = 0
w2 = 0

epochs = 300
for epoch in range(1, epochs + 1):
    for i in range(len(x1)):
        predict = w1 * x1[i] + w2 * x2[i] + w0
        w1 += 2 * lr * x1[i] * (y[i] - predict)
        w2 += 2 * lr * x2[i] * (y[i] - predict)
        w0 += 2 * lr * (y[i] - predict)

print(f'w0 = {w0}, w1 = {w1}, w2 = {w2}')

#w0 = -0.6915148481153723, w1 = 2.9955375929534673, w2 = 2.0175643492358
