import matplotlib.pyplot as plt

delivery_times = [32, 28, 45, 30, 36, 40, 29, 34, 38, 31,
                  27, 44, 33, 35, 39, 37, 44, 30, 29, 32,
                  36, 28, 43, 31, 35, 40, 38, 33, 30, 42]

plt.hist(delivery_times)

plt.title('Swiggy Delivery Times')
plt.xlabel('Delivery Time (Minutes)')
plt.ylabel('Number of Orders')

plt.show()