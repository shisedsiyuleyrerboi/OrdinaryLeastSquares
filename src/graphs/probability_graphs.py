import matplotlib.pyplot as plt
import numpy as np
from variables import *
from parts import part3

x = np.linspace(mean - 4*sd, mean + 4*sd, 500)

y1 = stats.norm.pdf(x, loc=mean, scale=sd)

mean2 = mean + 0.3
sd2 = sd * 0.9
y2 = stats.norm.pdf(x, loc=mean2, scale=sd2)

plt.figure(figsize=(10, 5))

plt.plot(x, y1, label='Distribution 1', linewidth=2)
plt.plot(x, y2, label='Distribution 2', linewidth=2)

plt.axvline(0, color='gray', linestyle='--', alpha=0.8)
plt.axvline(0.2, color='gray', linestyle='--', alpha=0.8)

plt.title('Probability Distributions')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()