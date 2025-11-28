from variables import *

prices = []

for contract, k in strike:
    d1 = ((np.log(S0 / k)) + (r + 1/2 * var)* T) / sd * np.sqrt(T)
    d2 = d1 - sd * np.sqrt(T)

    if contract  == 'call':
        price = S0 * stats.norm.cdf(d1) - k * np.exp(-r * T) * stats.norm.cdf(d2)
    else:
        price = k * np.exp(-r * T) * stats.norm.cdf(-d2) - S0 * stats.norm.cdf(-d1)
    
    prices.append(price)
    print(f'Type of Contract : {contract}, Strike Price = {k} , Delta 1 = {d1:.4f} , Delta 2 = {d2:.4f}')