import numpy as np
import astropy
from astropy import units as u 
from astropy.constants import G

# Converting Gravitational Constant to a pure value without units
G = G.to_value()

# Welcome Message :)
print("Welcome to my Gravitational Acceleration Calculator")

# Mass in kg
mass = float(input("What is the mass of your object in kg? "))

# Distance in km 
distance = 1000*float(input("What is the distance from the mass in km? "))

# Equation for gravitational force
Gravitational_Acceleration = ((G*mass)/(distance**2))
print("The gravitatonal acceleration", Gravitational_Acceleration,"m/s^2")
