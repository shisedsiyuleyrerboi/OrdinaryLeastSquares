from variables import *

values = [0, 75, 85]

for i in values:
    if i <= 0:
        print(f'P(logN(St) < logN({i})) : LogN must be always positive')
        continue
    
    z = (np.log(i / S0) - mean) / sd
    prob = stats.norm.cdf(z)

    print(f'P(St < {i}) = {prob:.4f}')