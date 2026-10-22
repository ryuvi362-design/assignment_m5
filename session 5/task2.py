import matplotlib.pyplot as plt
import numpy as np

scores = np.random.randint(120, 221, 50)

plt.hist(scores, bins=5, color='skyblue')

plt.title('IPL Match Scores - 5 Bins')
plt.xlabel('Scores')
plt.ylabel('Frequency')

plt.show()

plt.hist(scores, bins=10, color='orange')

plt.title('IPL Match Scores - 10 Bins')
plt.xlabel('Scores')
plt.ylabel('Frequency')

plt.show()