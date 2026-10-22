import matplotlib.pyplot as plt

steps = [3000, 4500, 5000, 6000, 7000, 8000, 5500,
         6500, 9000, 10000, 7500, 8500, 4000, 5000,
         6500, 7000, 8000, 9500, 11000, 6000, 7500,
         8500, 9000, 5500, 6500, 7000, 8000, 10000,
         12000, 9000]

plt.hist(steps, bins=5, color='green')

plt.title('Daily Steps - Frequency')
plt.xlabel('Steps')
plt.ylabel('Frequency')

plt.show()

plt.hist(steps, bins=5, density=True, color='purple')

plt.title('Daily Steps - Density')
plt.xlabel('Steps')
plt.ylabel('Density')

plt.show()