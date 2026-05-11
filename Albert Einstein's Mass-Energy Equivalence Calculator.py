import numpy as np
from astropy.constants import c

# Convert speed of light (c) to pure value without units
c = c.to_value()

# Mass in kg
mass = float(input("What is the mass of your object in kg? "))

# Equation for E=mc^2
Energy = mass*((c)**2)

print("Total Energy output = ",Energy," Joules")
