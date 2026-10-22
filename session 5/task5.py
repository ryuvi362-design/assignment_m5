import matplotlib.pyplot as plt

prices = [150, 250, 400, 550, 700, 900,
          1200, 1500, 1800, 2200, 2500,
          3000, 3500, 4000, 4500, 5000]

bins = [100, 501, 1001, 2001, 5001]

plt.hist(prices, bins=bins, color='pink', edgecolor='black')

plt.title('Flipkart Product Prices')
plt.xlabel('Price (Rs)')
plt.ylabel('Number of Products')

plt.xticks([100, 501, 1001, 2001, 5001])

plt.show()