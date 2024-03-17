import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Загрузка данных
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # один признак
y = 4 + 3 * X + np.random.randn(100, 1)  # целевая переменная с небольшим шумом

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

# Создание и обучение модели линейной регрессии
scaler = StandardScaler()# нормализация данных
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание
y_pred = model.predict(X_test)
# Вычисление среднеквадратичной ошибки
mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error:", mse)

plt.scatter(X_train, y_train, c='green', label='Обучающие данные')
plt.scatter(X_test, y_test, c='red', label='Тестовые данные')
plt.plot(X_test, y_pred, c='blue', label='Линия регрессии')

plt.xlabel('Признак')
plt.legend('целевая переменная')
plt.legend()
plt.show()
