import platform
import os

if platform.system() == 'Windows':
    os.system('cls')
elif platform.system() in ['Darwin', 'Linux']:
    os.system('clear')

print('PART I')
from parts import part1

print('\nPART II')
from parts import part2

print('\nPART III')
from parts import part3

# PAYOFFS AND PROFITS # 
from graphs import payoff_graphs
from graphs import profit_graphs
from graphs import probability_graphs