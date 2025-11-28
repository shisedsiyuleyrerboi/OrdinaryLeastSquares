import matplotlib.pyplot as plt
from parts import part3
from variables import *
import numpy as np

K_call = strike[0][1]
K_put = strike[1][1]

call_price = part3.prices[0]
put_price = part3.prices[1]

ST = np.linspace(0, 150, 1000)

payoff_call = np.maximum(ST - K_call, 0)
profit_call = payoff_call - call_price

payoff_put = np.maximum(K_put - ST, 0)
profit_put = payoff_put - put_price

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(ST, profit_call, 'b-', linewidth=2, label='Profit/Loss')
axes[0].axhline(y=0, color='k', linestyle='-', linewidth=0.5)
axes[0].axvline(x=K_call, color='r', linestyle='--', linewidth=1)
axes[0].fill_between(ST, profit_call, 0, where=(profit_call >= 0), alpha=0.3, color='green', label='Profit')
axes[0].fill_between(ST, profit_call, 0, where=(profit_call < 0), alpha=0.3, color='red', label='Loss')
axes[0].set_xlabel('ST')
axes[0].set_ylabel('Profit/Loss')
axes[0].set_title(f'Call Profit (K={K_call}, Premium={call_price:.4f})')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(ST, profit_put, 'g-', linewidth=2, label='Profit/Loss')
axes[1].axhline(y=0, color='k', linestyle='-', linewidth=0.5)
axes[1].axvline(x=K_put, color='r', linestyle='--', linewidth=1)
axes[1].fill_between(ST, profit_put, 0, where=(profit_put >= 0), alpha=0.3, color='green', label='Profit')
axes[1].fill_between(ST, profit_put, 0, where=(profit_put < 0), alpha=0.3, color='red', label='Loss')
axes[1].set_xlabel('ST')
axes[1].set_ylabel('Profit/Loss')
axes[1].set_title(f'Put Profit (K={K_put}, Premium={put_price:.4f})')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()