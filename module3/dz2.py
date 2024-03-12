import matplotlib.pyplot as plt
X = [1, 3, 7]
y = [2, 6, 14]
w1 = 1.5
w0 = 0.7
lr = 0.01
for i in range(222):
    for i in range(len(X)):
        prediction = w1*X[i] + w0
        w1 += 2 * lr * X[i] * (y[i] - prediction)
        w0 += 2 * lr * (y[i] - prediction)
print(w1, w0)


plt.scatter(X, y, color='red')
plt.plot(X, y)
plt.grid()
plt.show()
k = 2 #тангенс
b = 0 #смещение
print("k = 2, b = 0")
print(f"w1 = {w1}, w0 = {w0}")
print("Вроде весы похожи на настоящие")