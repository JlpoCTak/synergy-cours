import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# plt.plot([1, 2, -1],[3, 7, 9])
# plt.show()


def parable(x):
    return x**2


# x = np.array([1, 2, 3])
# y = parable(x)
#
# plt.plot(x,y)
# plt.show()

# x = np.linspace(1, 10, 300)
# y = parable(x)
# plt.plot(x, y)
# plt.grid()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Parable')
# plt.show()

# x = np.linspace(0, 6, 100)
# plt.figure(figsize=(10, 5))
# plt.plot(x, np.sin(x), linewidth=2, color='g', dashes=[8, 4, 2, 4], label='sin(x)', alpha=0.5)
# plt.show()

# plt.plot(x, np.cos(x),  linewidth=2, color='r', dashes=[8, 4, 2, 4], label='sin(x)', alpha=0.5)
# plt.xticks(np.linspace(0, 6, 3), ('0', '1', '2'), fontsize=20) #подписи оси х, (по оси у .yticks)
# plt.show()

# x = np.random.rand(100) #от 0 до 1, 100 точек
# y = np.random.rand(100)
# color = np.random.rand(100)
# sizes = 1000 * np.random.rand(100)
# plt.scatter(x, y, c=color, s=sizes, alpha=0.5)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# data = np.random.randn(1000)
# plt.hist(data, bins=10, color='g')
# plt.show()

# categ = ['a', 'b', 'c']
# count = [45, 209, 20]
# # plt.bar(categ, count)
# plt.pie(count, labels=categ, autopct='%1.1f%%')
# plt.show()

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
plt.show()
