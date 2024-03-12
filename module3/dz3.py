import matplotlib.pyplot as plt
lr = 0.01
w0 = 0.379008
w1 = 1.945856
x= [1,3,7]
y= [2,6,14]

for i in range(len(x)):
  predict = w1*x[i]+w0
  w1 += 2 * lr * x[i] * (y[i] - predict)
  w0 += 2 * lr * (y[i] - predict)
print(f'w0 = {w0}, w1 = {w1}')
plt.scatter(x,y,color= 'red')
plt.plot([0,8],[w0,8*w1+w0])
plt.grid()
plt.show()