import matplotlib.pyplot as plt
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

x = np.linspace(0, 6, 100)
plt.figure(figsize=(10, 5))
plt.plot(x, np.sin(x), linewidth=2, color='g', dashes=[8, 4, 2, 4], label='sin(x)', alpha=0.5)
plt.show()



