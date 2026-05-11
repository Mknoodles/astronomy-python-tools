import numpy as np
import astropy
from astropy import units as u 
from astropy.constants import G

# Converting Gravitational Constant to a pure value without units
G = G.to_value()

# Mass in kg
mass = float(input("What is the mass of your object in kg? "))

# Mass 2 in kg
mass_2 = float(input("What is the mass of object 2 in kg? "))

# Distance
distance = 1000*float(input("What is the distance between the two masses in km?"))

# Equation for gravitational force
Gravitational_Force = (G*((mass*mass_2)))/(distance**2)
print("The force of gravity is", Gravitational_Force)
