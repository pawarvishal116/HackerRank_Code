import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")  # Options: whitegrid, dark, white, ticks

x=np.array([1, 2, 3, 4, 5])
y = np.sin(x)

sns.lineplot(x=x, y=y)
plt.title('Beautiful Line Plot')
plt.show()
