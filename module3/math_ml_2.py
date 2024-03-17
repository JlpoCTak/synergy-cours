import numpy as np
import matplotlib.pyplot as plt

def linear_regression(X, y, X_test, y_test, lr=0.1, epochs=50):
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    w0 = 0
    mse_train = []
    mse_test = []
    for i in range(epochs):
        #делаем предсказания для всех наблюдений
        y_pred = X @ weights + w0
        #меняем веса
        weights += 2 * lr * (1 / n_samples) * X.T @ (y-y_pred)
        w0 += 2 * lr * (1 / n_samples) * np.sum(y - y_pred)
        y_train_pred = X @ weights + w0
        mse_train.append(mean_squared_error(y_train, y_train_pred))
        y_test_pred = X_test @ weights + w0
        mse_train.append(mean_squared_error(y_test, y_test_pred))
    return weights, w0, mse_train, mse_test


def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def predict(X, weights, w0):
    return X @ weights + w0


# y = 50x1 + 12x2 + 6x3 - 100
N = 100
M = 3
X = np.random.randint(1, 10, (N, M))
w_real = np.array([50, 12, -6])
w0 = -100
y = X @ w_real + w0
X = (X - X.mean(axis=0)) / X.std(axis=0)
X_train = X[:80, :]
X_test = X[80:, :]
y_train = y[:80]
y_test = y[80:]
weights, w0, mse_train, mse_test = linear_regression(X_train, y_train, X_test, y_test)
y_pred = predict(X_test, weights, w0)

mse = mean_squared_error(y_test, y_pred)
print(mse)

# print(y_pred)
# print(y_test)

plt.plot(range(len(mse_train)), mse_train, label='Train Set')
plt.plot(range(len(mse_test)), mse_test, label='Test Set')
plt.legend()
plt.show()

class Custom_Linear_Regression:
    def __init__(self, lr=0.1, epochs=50):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.w0 = None
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.w0 = 0
        for i in range(self.epochs):
            # делаем предсказания для всех наблюдений
            y_pred = X @ self.weights + self.w0
            # меняем веса
            self.weights += 2 * self.lr * (1 / n_samples) * X.T @ (y - y_pred)
            self.w0 += 2 * self.lr * (1 / n_samples) * np.sum(y - y_pred)
    def predict(self, X):
        return X @ self.weights + self.w0

N = 100
M = 3
X = np.random.randint(1, 10, (N, M))
w_real = np.array([50, 12, -6])
w0 = -100
y = X @ w_real + w0
X = (X - X.mean(axis=0)) / X.std(axis=0)
X_train = X[:80, :]
X_test = X[80:, :]
y_train = y[:80]
y_test = y[80:]

model = Custom_Linear_Regression(lr=0.01)
model.fit(X_train, y_train)
y_pred = model.predict
print(mean_squared_error(y_test, y_pred))
