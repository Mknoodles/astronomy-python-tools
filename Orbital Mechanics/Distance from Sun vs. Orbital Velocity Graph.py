import numpy as np
import matplotlib.pyplot as plt

# Range of x-values
x = np.linspace(0.01, 100, 100)

# Equation
a = np.sqrt(x**3)   # Equation for P(years)
b = x*2*np.pi       # Equation for circumference
c = b*149597871     # Convert AU to KM
d = a*31536000      # Convert P(years) to s(seconds)
e = c/d             # Equation for velocity (km/s)


# Plot Visuals
plt.figure(figsize=(8, 6))
plt.plot(x, e, label='KM/s/AU')

# Plot labels
plt.xlabel('Distance from Sun (AU)')
plt.ylabel('Velocity (KM/s)')
plt.title('Distance from Sun vs. Orbital Velocity')
plt.grid(True)
plt.legend()
plt.show()
