import numpy as np
import matplotlib.pyplot as plt

# Range of x-values
x = np.linspace(0.01, 100, 100)

# Equation
y = np.sqrt(x**3)

# Plot Visuals
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$P(years) = \U0000221A{(AU)^3}$')

# Plot labels
plt.xlabel('AU')
plt.ylabel('Years')
plt.title('Distance from Sun vs. Orbital Period')
plt.grid(True)
plt.legend()
plt.show()