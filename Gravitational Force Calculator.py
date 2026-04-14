import numpy as np
import astropy
from astropy import units as u 
from astropy.constants import G

# Placeholder before I figure out scientific notation for astropy
print("Input your numbers without the scientific notater. You can tack on the scientific notation after you input your mass")

# Mass in kg
mass = float(input("What is the mass of your object in kg? "))

# Scientific notation exponent
scientific_notation_modifier_mass_exponent = float(input("What is the exponent for your scientific notater? "))

# Scientific notation base and exponent
scientific_notation_modifier_mass = float(10**scientific_notation_modifier_mass_exponent)

# Mass 2 in kg
mass_2 = float(input("What is the mass of object 2 in kg? "))

# Scientific notation exponent 2
scientific_notation_modifier_mass_exponent_2 = float(input("What is the exponent for your 2nd scientific notater? "))

# Scientific notation base and exponent 2
scientific_notation_modifier_mass_2 = float(10**scientific_notation_modifier_mass_exponent_2)

# Mass redefined with scientific notation
mass = mass * scientific_notation_modifier_mass
mass_2 = mass_2 * scientific_notation_modifier_mass_2

# Distance
distance = 1000*float(input("What is the distance between the two masses in km?"))

# Equation for gravitational force
Gravitational_Force = (G*((mass*mass_2)))/(distance**2)
print("The force of gravity is", Gravitational_Force)