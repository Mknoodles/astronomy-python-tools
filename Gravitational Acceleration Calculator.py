import numpy as np
import astropy
from astropy import units as u 
from astropy.constants import G

# Welcome Message :)
print("Welcome to my Gravitational Acceleration Calculator")

# Placeholder before I figure out scientific notation for astropy
print("Input your numbers without the scientific notater. You can tack on the scientific notation after you input your mass")

# Mass in kg
mass = float(input("What is the mass of your object in kg? "))

# Scientific notation exponent
scientific_notation_modifier_mass_exponent = float(input("What is the exponent for your scientific notater? "))

# Scientific notation base and exponent
scientific_notation_modifier_mass = float(10**scientific_notation_modifier_mass_exponent)

# Mass redefined with scientific notation
mass = mass * scientific_notation_modifier_mass

# Distance in km 
distance = 1000*float(input("What is the distance from the mass in km? "))

# Equation for gravitational force
Gravitational_Acceleration = ((G*mass)/(distance**2))
print("The gravitatonal acceleration", Gravitational_Acceleration)