import matplotlib.pyplot as plt
import regression_engine

fitted = regression_engine.model.fittedvalues
y = regression_engine.y

plt.figure(figsize=(8,6))

plt.scatter(fitted, y, alpha=0.8, label='Data')

min_val = min(fitted.min(), y.min())
max_val = max(fitted.max(), y.max())
plt.plot([min_val, max_val], [min_val, max_val], 'b:', label = 'Regression Line')

plt.xlabel('Expected ROE')
plt.ylabel('Actual ROE')
plt.grid(True)
plt.legend()
plt.show()