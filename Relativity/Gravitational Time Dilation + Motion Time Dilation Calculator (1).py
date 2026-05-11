import numpy as np
import astropy
import astropy.units as u
from astropy.constants import M_earth
from astropy.constants import c, G

# Welcome messages and guide
print("Welcome to the Time Dilation Calculator!")


# Mass input
mass = float(input("What is the mass of the object? (input value in kg) "))
distance = float(input("What is the distance from the object? (input value in km) "))

# Earth time dilation factor for comparison
earth_dilation_factor = np.sqrt(1-((2*G.to_value()*M_earth.to_value())/(6371*1000*(c.to_value()**2))))

# gravity time dilation
gravity_dilation_factor = np.sqrt(1-((2*G.to_value()*mass)/(distance*1000*(c.to_value()**2))))

# Velocity Variable
velocity = float(input("What is the velocity of your object? (input value in m/s) "))

# Motion dilation factor
gamma = 1/np.sqrt(1-((velocity**2)/(c.to_value()**2)))

# Combined factor
combined_factor = gravity_dilation_factor*(1/gamma)

# Converting proper time (t1) into observed time (t2)
proper_time = float(input("How much time passed near the object? (input value in seconds) "))
earth_time = proper_time/combined_factor

# Time difference
time_difference = earth_time-proper_time
print("Combined factor =",combined_factor)
print("For",proper_time,"second(s) near the object",earth_time,"passed on Earth")
print("That is a",time_difference,"in time")
