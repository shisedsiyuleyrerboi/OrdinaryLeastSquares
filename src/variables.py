import scipy.stats as stats
import numpy as np

S0 = 80
mean = 0.1
sd = 0.25
var = sd**2
strike = [('Call', 85) , ('Put', 75)] 
T = 1
r = 0.05