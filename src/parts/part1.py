from variables import *

values_p1 = [0, 0.2]

prob_1 = stats.norm.cdf(values_p1[0], loc=mean, scale=sd)
prob_2 = 1 - stats.norm.cdf(values_p1[1], loc=mean, scale=sd)

print(f'P(R < 0.0)   = {prob_1:.4f}')
print(f'P(R > 0.2)   = {prob_2:.4f}')