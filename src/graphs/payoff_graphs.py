import matplotlib.pyplot as plt
import numpy as np
from variables import *

K_call = strike[0][1]
K_put = strike[1][1]

ST = np.linspace(0, 150, 1000)

payoff_call = np.maximum(ST - K_call, 0)
payoff_put = np.maximum(K_put - ST, 0)
payoff_underlying_asset = ST

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].plot(ST, payoff_call, 'b-', linewidth=2)
axes[0].axhline(y=0, color='k', linestyle='-', linewidth=0.5)
axes[0].axvline(x=K_call, color='r', linestyle='--', linewidth=1)
axes[0].set_xlabel('ST')
axes[0].set_ylabel('Payoff')
axes[0].set_title(f'Payoff Call (K={K_call})')
axes[0].grid(True, alpha=0.3)

axes[1].plot(ST, payoff_put, 'g-', linewidth=2)
axes[1].axhline(y=0, color='k', linestyle='-', linewidth=0.5)
axes[1].axvline(x=K_put, color='r', linestyle='--', linewidth=1)
axes[1].set_xlabel('ST')
axes[1].set_ylabel('Payoff')
axes[1].set_title(f'Payoff Put (K={K_put})')
axes[1].grid(True, alpha=0.3)

axes[2].plot(ST, payoff_underlying_asset, 'orange', linewidth=2)
axes[2].axhline(y=0, color='k', linestyle='-', linewidth=0.5)
axes[2].set_xlabel('ST')
axes[2].set_ylabel('Payoff')
axes[2].set_title('Payoff Underlying Asset')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()