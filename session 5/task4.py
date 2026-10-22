import matplotlib.pyplot as plt
import numpy as np

duration = np.random.randint(120, 301, 50)

plt.hist(duration, bins=10, color='purple')

plt.title('Spotify Song Duration Distribution')
plt.xlabel('Song Duration (Seconds)')
plt.ylabel('Frequency')

plt.show()